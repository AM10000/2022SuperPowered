#!/usr/bin/env micropython
from Kronos import *
import math
from ev3dev2.sensor import *
from ev3dev2.sound import *
from ev3dev2.console import *
from ev3dev2.motor import *

k = Kronos()
scr = Console()

#positive degrees is down
k.moveDistance(-15, -15, 2)
k.moveDistance(-15, -15, 25)
k.LmediumMotorDegrees(100, 2300)
k.moveDistance(-100, -100, 5)