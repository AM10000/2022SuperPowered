#!/usr/bin/env micropython
from Kronos import *
from ev3dev2.sensor import *
k = Kronos()


k.lfCColorRangeL(20, True, 45, 47)

k.spinRobot(20, -20, 60)