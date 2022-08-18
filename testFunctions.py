#!/usr/bin/env micropython
from Kronos import *
from ev3dev2.sensor import *
k = Kronos()

k.LmediumMotorDegrees(60, 200)
k.squareToBlack(15)
