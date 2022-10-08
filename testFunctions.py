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
k.LmediumMotorDegrees(100, 2000)
k.moveDistance(-100, -100, 1)
k.LmediumMotorDegrees(100, 200)