"""
Im trying to predict Matty's time to run 110 yards and back on a soccer field
July 17, 2024
"""

# Returns displacement given initial velocity, acceleration, and time
def displacementWithTime(v_initial,time,acc):
	return v_initial*time + 0.5*acc*(time**2)

# Returns displacement given final and initial velocities and acceleration
def displacementWithoutTime(v_initial,v_final,acc):
	return (v_final**2-v_initial**2)/(2*acc)

