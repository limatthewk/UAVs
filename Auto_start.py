import sys
sys.path.append(r"c:\Python27\Lib")
import clr
import serial
import time
import datetime
import MissionPlanner #import
clr.AddReference("MAVLink")
import MAVLink
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp
'''This program will automatically start Mission Planner flight path, return UAV's waypoint number, latitude, longitde,
altitude right before it passes the waypoint, and print distance to next waypoint after it passes its current waypoint'''

# Auto mission start
Script.ChangeMode('Manual')
if cs.mode != 'Auto':		# Setting Mode to Auto
  Script.ChangeMode('Auto')
  print'Starting mission\n'
  MAV.setParam('wpno',1)	# Initializing mission start at 1
  
# Prints the passed waypoint number and the plane's latitude, longitude and altitude each time the plane reaches the waypoint
# Print current distance to next waypoint after passing previous waypoint
currentWP = Script.getParam('wpno')
WPcount = getWPCount()
while currentWP < WPcount:
	wpdist1 = cs.wp_dist
	if wpdist1 < (Script.GetParam('WP_RADIUS') + 10):
		currentWP = Script.getParam('wpno')
		print currentWP
		print cs.lat
		print cs.long
		print cs.alt
		time.sleep(1)
		print cs.wp_dist