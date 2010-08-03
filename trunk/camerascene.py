from PyQt4 import Qt,QtGui,QtCore
import uc480

class CameraScene(QtGui.QGraphicsScene):
	def __init__(self,parent):
		QtGui.QGraphicsScene.__init__(self,parent)
		self.scan_line = QtCore.QLineF(10,10,20,20)
		self.addLine(self.scan_line)
		self.timer = Qt.QTimer(parent)
		QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"),self.refresh)
		self.new_selection = False
		
	def start_camera(self):
		self.camera = uc480.camera()
		self.camera.AllocImageMem()
		self.camera.SetImageMem()
		self.camera.SetImageSize()
		self.camera.SetColorMode()
		self.camera.CaptureVideo()
		self.camera.CopyImageMem()
		self.image = QtGui.QImage(self.camera.data.ctypes.data,	self.camera.width,self.camera.height,QtGui.QImage.Format_Indexed8)
		color_table = [QtGui.qRgb(i,i,i) for i in range(0,256)]	 
		self.image.setColorTable(color_table)	
		self.setBackgroundBrush(QtGui.QBrush(self.image.scaledToHeight(self.height())))
		self.timer.start(100)
			
	def stop_camera(self):
		self.timer.stop()
		self.camera.StopLiveVideo()
		self.camera.FreeImageMem()
		self.camera.ExitCamera()
			
	def refresh(self):
		self.camera.CopyImageMem()
		self.setBackgroundBrush(QtGui.QBrush(self.image.scaledToHeight(self.height())))
				
	def mousePressEvent(self,event):
		if self.parent().findChild(QtGui.QRadioButton,"select_line_button").isChecked():
			self.clear()
			self.addLine(QtCore.QLineF())
			self.selection = lambda event: self.items()[0].setLine(QtCore.QLineF(event.buttonDownScenePos(QtCore.Qt.LeftButton),event.lastScenePos()))
			self.new_selection = True
			self.selection(event)
		elif self.parent().findChild(QtGui.QRadioButton,"select_area_button").isChecked():
			self.clear()
			self.addRect(QtCore.QRectF())
			self.selection = lambda event: self.items()[0].setRect(QtCore.QRectF(event.buttonDownScenePos(QtCore.Qt.LeftButton),event.lastScenePos()))
			self.selection(event)
			self.new_selection = True
		
	def mouseMoveEvent(self,event):
		if self.new_selection:
			self.selection(event)
		print event.scenePos()

	def mouseReleaseEvent(self,event):
		if self.new_selection:
			self.selection(event)
			self.new_selection = False

		
		