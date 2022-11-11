#!/usr/bin/env micropython
from Kronos import *
import math
from ev3dev2.sensor import *
from ev3dev2.sound import *
from ev3dev2.console import *
from ev3dev2.motor import *

k = Kronos()
scr = Console()

k.moveDistance(40, 40, 16)
k.moveUntilColorgt(0, 15, INPUT_2, 80)
k.moveUntilColorlt(0, 15, INPUT_2, 16)
k.moveDistance(20, 20, 3)
k.LmediumMotorDegrees(70, 210)