import numpy as np
import nidaqmx
import niscope

class OctEngine:
	def __init__(self):
		self.setCentralWavelength()
		self.number_ascans_per_line = 500
		self.point_per_ascan = 1000
		self.ascan_rate = 20000
		self.raw_line_scan_data = np.zeros((2,self.number_scans_per_line),dtype=np.int16)
		self.resampled_data = np.zeros((2,self.number_scans_per_line),dtype=np.float(64))
		self.initializeScope()

	def initializeScope(self):
		self.scope = niscope.Scope()
		sample_rate = self.point_per_ascan*self.ascan_rate
		self.scope.ConfigureHorizontalTiming(sample_rate,self.point_per_ascan,0.5,self.number_ascans_per_line)
		self.scope.ConfigureVertical(channelList="0,1",range=10)
		self.scope.ConfigureTrigger(trigger_type='Digital',
									triggerSource = "External",
									slope = "raising",
									holdoff = 30,
									delay = 0)
		self.scope.Commit()
	
	def setWavelengthRange(self,start_wavelength,stop_wavelength):
		self.start_wavelength = start_wavelength
		self.stop_wavelength = stop_wavelength
		
	def setCentralWavelength(self,central_wavelength=1300.0):
		self.central_wavelength = central_wavelength
	
	def acquireReferenceInterferogram(self,channel="1"):
		pass
		
	def loadReferenceInterferogram(self,filename="reference_interferogram.dat"):
		pass
		
	def fitPointSpacingToOpticalFrequencyCurve(self):
		pass
		
	def resampleAScan(self,data):
		pass
		
	def resampleLineScan(self):
		pass
	
	def setLineScanTask(self,start_point,stop_point):
		start_voltage.x = start_point.x/self.distance_to_voltage
		stop_voltage.x = stop.point.x/self.distance_to_voltage
		start_voltage.y = start_point.y/self.distance_to_voltage
		stop_voltage.y = stop.point.y/self.distance_to_voltage
		
		voltage_x = np.linspace(start_voltage.x,stop_voltage.x,num_galvo_scan_samples)
		voltage_y = np.linspace(start_voltage.y,stop_voltage.y,num_galvo_scan_samples)
		self.forward_task = nidaqmx.AnalogOutputTask("Dev1")
		self.forward_task = create_voltage_channel("AO0,AO1", channel_name="forward",
                               min_val = -1, max_val = 1, 
                               units = 'volts', custom_scale_name = None)
		#self.forward_task.set_sample_clock_rate(self.sample_rates)
		
		pass
	
	def setAreaScanRect(self,upper_left,bottom_right):
		pass
		
	def setDistanceToVoltage(self,distance,voltage):
		pass
		
	def scanLine(self):
		self.scanGalvo()
		self.scope.InitiateAcquisition()
		##wait till finish code
		self.scope.CopyTo(self.raw_line_scan_data)
		self.resample(self.raw_line_scan_data)
		self.FFT(self.resampled_data)
		
		
	def scanArea(self):
		pass
		
	def scanGalvo(self,direction="forward"):
	
		
		
	def setNumberOfScanPoints(self,numberf_of_points):
		pass
		
	def setNumberOfLineScans(self,number_of_line_scans):
		pass
		
	def switch(self):
		#referenceInterferogram
		#galvoPosition x
		#galvoPosition y
		
if __name__ == "__maint__":
	oct = OctEngine()
	while True:
		print "1: Scan Line"
		print "q: Quit"
		sel = raw_input("Select option:")
		if sel == 'q': break
		elif sel == '1': oct.scanLine()
	
	oct.close()
	