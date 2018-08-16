import time

help = "Firmware Version 1.51\n? Short Status\n+ Full Engineering Status\nST Stop all motion\nCL Close Main Door\nOP Open Main Door\nUP Close (raise) Dropout Door\nDN Open (lower) Dropout Door\nSO Synchronized Open (Both doors open together)\nSC Synchronized Close (Both doors close together)\nAO Auto shutdown ON\nAF Auto shutdown OFF\nRO Rain ON\nRF Rain OFF\nCO Cloud Sensor ON\nCF Cloud Sensor OFF\nHM Rotate to home position\nd MV Move to Azimuth (d=degrees, 0.0 ≤ d < 360)\nd TOL Tolerance (0.0 ≤ d < 3 degrees)\nd HZ Define home position (0 ≤ d < 360 degrees)\nd HS High speed threshold (0 ≤ d < 10 degrees)\nd CS Coast (0 ≤ d < 6 degrees)\nd LM Encoder counts for 360 degrees\nt WT Watchdog Timer (t = seconds, 600 typical)\nt RD Set reverse direction motion delay (t ≤ 0 ≤ 6 seconds)\nCFS Save current configuration\nCFR Recall last saved configuration\nHELP Display this list of available commands\n>\n"
shortStatus = "MAIN %s %d\nDROP %s %d\n[%s] %s\n%s %.2f\n%s %d"
EngineeringStatus = "Emergency Stop Active: %d\nSCB radio link OK: %d\nHome Azimuth: %.2f\nHigh Speed (degrees): %.2f\nCoast (degrees): %.2f\nTolerance (degrees): %.2f\nEncoder Counts per 360: %d\nEncoder Counts: %d\nLast Azimuth GoTo: %.2f\nRain-Snow enabled: %d\nCloud Sensor enabled: %d\nWatchdog Reset Time: %d\nDropout Timer: %d\nReverse Delay: %d\nMain Door Encoder Closed: %d\nMain Door Encoder Opened: %d\nDropout Encoder Closed: %d\nDropout Encoder Opened: %d"

azimuthSpeed = 2
mainShutterSpeed = 2
dropoutSpeed = 2

class DomeSimulator:
	def __init__(self):
		self.mainShutterPosition = 35
		self.dropoutShutterPosition = 0
		self.autoShutDown = 1
		self.sensorCode = 1
		self.azimuthPosition = 90.0
		self.lastRotation = 0
		self.motionCode = 20
		self.emergencyStopActive = 0
		self.SCBRadioLinkOK = 1
		self.homeAzimuth = 90.00
		self.highSpeed = 6.00
		self.coastValue = 0.20
		self.toleranceValue = 1.00
		self.encoderCountsPer360 = 490496
		self.enconderCounts = 1485289
		self.lastAzimuthGoTo = 90.0
		self.rainSnowEnabled = 1
		self.cloudSensorEnabled = 1
		self.watchdogResetTime = 600.0
		self.dropoutTimerValue = 100.0
		self.reverseDelay = 2.0
		self.mainDoorEncoderClosed = 1856
		self.mainDoorEncoderOpened = 456540
		self.dropoutEncoderClosed = 7156
		self.dropoutEncoderOpened = 10321
		
		#Commands
		self.lastAzimuthCommandTime = time.time()
		self.lastDropoutShutterCommandTime = time.time()
		self.lastMainShutterCommandTime = time.time()

		self.lastAzimuthCommand = self.azimuthPosition
		self.lastDropoutShutterCommand = self.dropoutShutterPosition
		self.lastMainShutterCommand = self.mainShutterPosition

		self.lastAzimuthCommandDirection = 1
		self.lastDropoutShutterCommandDirection = 1
		self.lastMainShutterCommandDirection = 1
		
		self.mainShutterMotionStatus = 0
		self.dropoutShutterMotionStatus = 0
		self.lastRotatioAzimuthStatus = "RR"
		self.currentRotatioAzimuthMotionStatus = 0
		self.seekingHome = 0
		
	def updateAzimuth(self):
		dt = self.getTime() - self.lastAzimuthCommandTime
		self.lastAzimuthCommandTime = self.getTime()
		
		self.azimuthPosition = self.azimuthPosition + dt*azimuthSpeed*self.lastAzimuthCommandDirection
		if(self.lastAzimuthCommandDirection > 0 and self.azimuthPosition > self.lastAzimuthCommand):
			self.azimuthPosition = self.lastAzimuthCommand
		if(self.lastAzimuthCommandDirection < 0 and self.azimuthPosition < self.lastAzimuthCommand):
			self.azimuthPosition = self.lastAzimuthCommand
			
		if(self.azimuthPosition < self.lastAzimuthCommand):
			self.currentRotatioAzimuthMotionStatus = 1
			self.lastRotatioAzimuthStatus = "RR"
		elif(self.azimuthPosition > self.lastAzimuthCommand):
			self.currentRotatioAzimuthMotionStatus = 2
			self.lastRotatioAzimuthStatus = "RL"
		elif(self.azimuthPosition == self.lastAzimuthCommand):
			self.currentRotatioAzimuthMotionStatus = 0
			self.seekingHome = 0
			
	def updateMainShutterMotionStatus(self):
	
		dt = self.getTime() - self.lastMainShutterCommandTime
		self.lastMainShutterCommandTime = self.getTime()
		self.mainShutterPosition = self.mainShutterPosition + dt*mainShutterSpeed*self.lastMainShutterCommandDirection
		if(self.lastMainShutterCommandDirection > 0 and self.mainShutterPosition > self.lastMainShutterCommand):
			self.mainShutterPosition = self.lastMainShutterCommand
		if(self.lastMainShutterCommandDirection < 0 and self.mainShutterPosition < self.lastMainShutterCommand):
			self.mainShutterPosition = self.lastMainShutterCommand
			
		if(self.mainShutterPosition < self.lastMainShutterCommand):
			self.mainShutterMotionStatus = 8
		elif(self.mainShutterPosition > self.lastMainShutterCommand):
			self.mainShutterMotionStatus = 4
		elif(self.mainShutterPosition == self.lastMainShutterCommand):
			self.mainShutterMotionStatus = 0
			
	def updateDropoutShutterMotionStatus(self):
		dt = self.getTime() - self.lastDropoutShutterCommandTime
		self.lastDropoutShutterCommandTime = self.getTime()
		self.dropoutShutterPosition = self.dropoutShutterPosition + dt*dropoutSpeed*self.lastDropoutShutterCommandDirection
		
		if(self.lastDropoutShutterCommandDirection > 0 and self.dropoutShutterPosition > self.lastDropoutShutterCommand):
			self.dropoutShutterPosition = self.lastDropoutShutterCommand
		if(self.lastDropoutShutterCommandDirection < 0 and self.dropoutShutterPosition < self.lastDropoutShutterCommand):
			self.dropoutShutterPosition = self.lastDropoutShutterCommand		
		
		if(self.dropoutShutterPosition < self.lastDropoutShutterCommand):
			self.dropoutShutterMotionStatus = 32
		elif(self.dropoutShutterPosition > self.lastDropoutShutterCommand):
			self.dropoutShutterMotionStatus = 16
		elif(self.dropoutShutterPosition == self.lastDropoutShutterCommand):
			self.dropoutShutterMotionStatus = 0	
			
	def updatePosition(self):	
		self.updateMainShutterMotionStatus()
		self.updateDropoutShutterMotionStatus()
		self.updateAzimuth()
		
	def getTime(self):
		return time.time()
		
	def getShortStatus(self):
		self.updatePosition()
		status = shortStatus%(self.getMainShutterStatus(),self.mainShutterPosition, self.getDropoutShutterStatus(), self.dropoutShutterPosition, self.autoShutdownStatus(),0,self.getPositionStatus(), self.azimuthPosition, self.lastRotatioAzimuthStatus, (self.seekingHome + self.mainShutterMotionStatus+self.dropoutShutterMotionStatus+self.currentRotatioAzimuthMotionStatus))
		return status
		
	def getEngineeringStatus(self):
		self.updatePosition()
		status = EngineeringStatus%(self.emergencyStopActive,self.SCBRadioLinkOK,self.homeAzimuth,self.highSpeed,self.coastValue, self.toleranceValue, self.encoderCountsPer360, self.enconderCounts, self.lastAzimuthGoTo, self.rainSnowEnabled, self.cloudSensorEnabled, self.watchdogResetTime,self.dropoutTimerValue, self.reverseDelay, self.mainDoorEncoderClosed, self.mainDoorEncoderOpened, self.dropoutEncoderClosed, self.dropoutEncoderOpened)
		return status	
		
	def getFullEngineeringStatus(self):
		result = self.getShortStatus()+"\n"+self.getEngineeringStatus()
		return result
		
	def getPositionStatus(self):
		homeStatus = "Home" if float(self.azimuthPosition) == float(self.homeAzimuth) else "Posn"
		return homeStatus
		
	def getMainShutterStatus(self):
		if(self.mainShutterPosition == 0):
			mainShutterStatus = "SHUT"
		elif(self.mainShutterPosition == 100):
			mainShutterStatus = "OPEN"
		else:
			mainShutterStatus = "AJAR"
		return mainShutterStatus
		
	def getDropoutShutterStatus(self):
		if(self.dropoutShutterPosition == 0):
			dropoutShutterStatus = "SHUT"
		elif(self.dropoutShutterPosition == 100):
			dropoutShutterStatus = "OPEN"
		else:
			dropoutShutterStatus = "AJAR"
		return dropoutShutterStatus
		
	def autoShutdownStatus(self):
		autoShutdown = "ON" if self.autoShutDown == 1 else "OFF"
		return autoShutdown
				
	def stopAllMotion(self):	
		return ""

	def closeMainDoor(self):
		self.lastMainShutterCommandTime = self.getTime()
		self.lastMainShutterCommand = 0
		self.lastMainShutterCommandDirection = -1	
		
	def openMainDoor(self):
		self.lastMainShutterCommandTime = self.getTime()
		self.lastMainShutterCommand = 100
		self.lastMainShutterCommandDirection = 1
		
	def closeDropoutDoor(self):
		self.lastDropoutShutterCommandTime = self.getTime()
		self.lastDropoutShutterCommand = 0
		self.lastDropoutShutterCommandDirection = -1
		
	def openDropoutDoor(self):
		self.lastDropoutShutterCommandTime = self.getTime()
		self.lastDropoutShutterCommand = 100
		self.lastDropoutShutterCommandDirection = 1
		
	def synchronizedOpen(self):
		self.openDropoutDoor()
		self.openMainDoor()
		
	def synchronizedClose(self):
		self.closeDropoutDoor()
		self.closeMainDoor()
		
	def autoShutdownON(self):
		self.autoShutDown = 1
		
	def autoShutdownOFF(self):
		self.autoShutDown = 0
	
	def rainON(self):
		self.rainSnowEnabled = 1
		
	def rainOFF(self):
		self.rainSnowEnabled = 0
		
	def cloudSensorON(self):
		self.cloudSensorEnabled = 1
		
	def cloudSensorOFF(self):
		self.cloudSensorEnabled = 0
	
	def rotateHomePosition(self):
		self.seekingHome = 64
		self.moveToAzimuth(self.homeAzimuth)
		
	def moveToAzimuth(self, azimuth):
		self.lastAzimuthGoTo = azimuth
		self.lastAzimuthCommandTime = time.time()
		self.lastAzimuthCommand = azimuth
		self.lastAzimuthCommandDirection = 1 if self.lastAzimuthCommand - self.azimuthPosition > 0 else -1
	
	def tolerance(self, toleranceValue):
		self.toleranceValue =  toleranceValue
		
	def defineHomePosition(self, azimuth):
		self.homeAzimuth = azimuth
	
	def highSpeedThreshold(self, threshold):
		self.highSpeed = threshold
		
	def coast(self, coastValue):
		self.coastValue = coastValue
		
	def encoderCountsFor360Degrees(self, count):
		self.encoderCountsPer360 = count
		
	def watchdogTimer(self,time):
		self.watchdogResetTime = time
		
	def setReverseDirectionMotionDelay(self, time):
		self.reverseDelay = time
		
	def saveCurrentConfiguration(self):
		pass
		
	def recallLastSavedConfiguration(self):
		return "The configuration is..."
		
	def displayHelp(self):
		return help
	
		
	def executeCommand(self, command):
		print(command)
		parseCmd = command.strip().split(" ")
		print(parseCmd)
		if(len(parseCmd) == 1):
			command = parseCmd[0]
			value = 0
		else:
			command = parseCmd[1]
			value = float(parseCmd[0])
			
		if(command == "ST"):
			self.stopAllMotion()
		elif(command == "CL"):
			self.closeMainDoor()
		elif(command == "OP"):
			self.openMainDoor()
		elif(command == "UP"):
			self.closeDropoutDoor()
		elif(command == "DN"):
			self.openDropoutDoor()
		elif(command == "SO"):
			self.synchronizedOpen()
		elif(command == "SC"):
			self.synchronizedClose()
		elif(command == "AO"):
			self.autoShutdownON()
		elif(command == "AF"):
			self.autoShutdownOFF()
		elif(command == "RO"):
			self.rainON()
		elif(command == "RF"):
			self.rainOFF()
		elif(command == "CO"):
			self.cloudSensorON()
		elif(command == "CF"):
			self.cloudSensorOFF()
		elif(command == "HM"):
			self.rotateHomePosition()
		elif(command == "MV"):
			self.moveToAzimuth(value)
		elif(command == "TOL"):
			self.tolerance(value)
		elif(command == "HZ"):
			self.defineHomePosition(value)
		elif(command == "HS"):
			self.highSpeedThreshold(value)
		elif(command == "CS"):
			self.coast(value)
		elif(command == "LM"):
			self.encoderCountsFor360Degrees(value)
		elif(command == "WT"):
			self.watchdogTimer(value)
		elif(command == "RD"):
			self.setReverseDirectionMotionDelay(value)
		elif(command == "CFS"):
			self.saveCurrentConfiguration()
			
	def queryStatus(self, type):
		if(type == "?"):
			return self.getShortStatus()+"\n>"
		elif(type == "+"):
			return "+\n"+self.getFullEngineeringStatus()+"\n>"
		elif(type == "CFR"):
			return self.recallLastSavedConfiguration()
		else:
			return self.displayHelp()
			