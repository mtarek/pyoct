from PyQt4.Qwt5 import Qwt
from octui import *
from PyQt4 import Qt,QtCore,QtGui
import sys
from camerascene import CameraScene
import numpy as np

class MainProgram(Ui_MainWindow):
	def __init__(self,MainWindow):
		self.setupUi(MainWindow)  
	
		self.camera_scene = CameraScene(MainWindow)
		self.camera_view.setScene(self.camera_scene)
		self.camera_scene.setSceneRect(QtCore.QRectF(self.camera_view.frameRect()))
		QtCore.QObject.connect(self.start_camera_button,QtCore.SIGNAL("clicked()")
												,self.start_camera_button_handle)
		self.setup_ascan_plot()
								
									
	def start_camera_button_handle(self):
		if self.start_camera_button.isChecked():
			self.camera_scene.start_camera()
		else:
			self.camera_scene.stop_camera()
			
	def setup_ascan_plot(self):
		plot = self.ascan_plot
		curve = Qwt.QwtPlotCurve("sin")
		curve.attach(plot)
		x = np.linspace(0,10,100)
		curve.setData(np.sin(x),x)
		plot.replot()
		
		
		
	
app = Qt.QApplication(sys.argv)
root = Qt.QMainWindow()
main_program = MainProgram(root)
root.show()
app.exec_()
#sys.exit()


