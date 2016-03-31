from math import sin, cos, atan2, sqrt, pi, asin
''' Generic functions for basic longitude/latitude/bearing/distance calculations. Based off of Haversine formula.
	See http://www.movable-type.co.uk/scripts/latlong.html for reference.'''

def conv_coord(degrees, minutes, seconds):
	# Converts any coordinate (degrees, minutes, seconds) to a decimal coordinate (degrees)
	
	coordinate = degrees + minutes/60.0 + seconds/3600.0
	return coordinate
	
def conv_bearing(degrees, minutes, seconds):
	# Converts any bearing (degrees, minutes, seconds) to a decimal bearing (degrees)

	bearing = degrees + minutes/60.0 + seconds/3600.0
	return bearing
    
def get_distance(lat1, lon1, lat2, lon2):
	# Returns the distance between 2 coordinates (lat1, lon1) and (lat2, lon2)
	
	lon1 = lon1*pi/180
	lon2 = lon2*pi/180
	lat1 = lat1*pi/180
	lat2 = lat2*pi/180
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	d = 6371 * c
	return d
    
def get_left_waypoint(lat, lon, yaw, radius):
    # Returns the coordinate the plane would go to if it dodged dead left of an obstacle
    
    return get_waypoint(lat, lon, yaw - pi / 2, radius)
    
def get_right_waypoint(lat, lon, yaw, radius):
    # Returns the coordinate the plane would go to if it dodged dead right of an obstacle
    # at (lat, lon) at a distance 'radius'.

    return get_waypoint(lat, lon, yaw + pi / 2, radius)
    
def get_bearing(lat1, lon1, lat2, lon2):
	# Returns the bearing (degrees( between a coordinate (lat1, lon1) facing another coordinate (la2, lon2)
	
	lon1 = lon1*pi/180
	lon2 = lon2*pi/180
	lat1 = lat1*pi/180
	lat2 = lat2*pi/180
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	x = sin(dlon)*cos(lat2)
	y = cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(dlon)
	bearing = atan2(x,y)
	return bearing * 180/pi % (360)
	
def get_waypoint(lat, lon, bearing, distance):
	#returns the target coordinate given initial coordinate (lat, lon), bearing (degrees) and distance

	lat = lat*pi/180
	lon = lon*pi/180
	bearing = bearing*pi/180
	s = distance/6371.0
	lat2 = asin(sin(lat)*cos(s)+cos(lat)*sin(s)*cos(bearing))
	lon2 = lon + atan2(sin(bearing)*sin(s)*cos(lat), cos(s)-sin(lat)*sin(lat2))
	return lat2*180/pi % 360, lon2*180/pi % 360
