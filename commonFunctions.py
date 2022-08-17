from ev3dev2.sensor.lego import *
from threading import Thread
from ev3dev2.motor import *
from ev3dev2.sensor import *

tank_drive=MoveTank(OUTPUT_A, OUTPUT_D)
def isInColorRange(floor, ceiling, port):
    cs = ColorSensor(address=port)
    if cs.reflected_light_intensity > floor and cs.reflected_light_intensity < ceiling:
        return True
    else:
        return False

def isNotInColorRange(_self, **kwargs):
    floor = kwargs['floor']
    ceiling = kwargs['ceiling']
    port = kwargs['port']
    if isInColorRange(floor, ceiling, port) == True:
        return False
    else:
        return True

def isInColorRange2(floor, ceiling, port1, port2):
    cs1=ColorSensor(address=port1)
    cs2=ColorSensor(address=port2)
    if cs2.reflected_light_intensity > floor and cs2.reflected_light_intensity < ceiling and cs1.reflected_light_intensity > floor and cs1.reflected_light_intensity < ceiling:
        return True
    else:
        return False

def isNotInColorRange2(_self, **kwargs):
    floor = kwargs['floor']
    ceiling = kwargs['ceiling']
    port1 = kwargs['port1']
    port2 = kwargs['port2']
    if isInColorRange2(floor, ceiling, port1, port2) == True:
        return False
    else:
        return True
# runs any given function in parallel
# the args should be passed in as a list ['a','b','c', 'etc']
# the function being called in parallel should declare its parameters 
# as it normally does
def runParallel(fnName, args):
    t = Thread(target=fnName, args=args)
    t.start()
'''
def calculateRadius(aSpeed, dSpeed, robotWidth):
    # if both speeds are 0 then raise an exception
    if(aSpeed==0 and dSpeed==0):
        raise Exception("Both speeds cannot be zero") 

    # check robot width
    if(robotWidth<=0):
        raise Exception("Invalid robot width")

    # Py is the higher speed
    # Px is the lower speed
    # if aSpeed and dSpeed are equal then the result is always 3 x robotWidth
    # assign Py and Px by comparing aSpeed and dSpeed
    if (aSpeed > dSpeed):
        Py = abs(aSpeed)
        Px = abs(dSpeed)
    else:
        Py = abs(dSpeed)
        Px = abs(aSpeed)

    if (Px==0 or Py==0):
        # return the radius as width of the robot
        return robotWidth

    return (robotWidth * ((3 * Py/Px)  + ((Py**2)/(Px**2)) + 2)) / (((Py**2)/(Px**2)) - (Py/Px) + 2)*20
'''