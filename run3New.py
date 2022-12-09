#!/usr/bin/env micropython
from Kronos import Kronos
from time import sleep
from ev3dev2.motor import SpeedPercent
k = Kronos()

# k.moveDistance(15, 15, 6)
# k.spinRobot(15, -15, 40)
# k.moveDistance(15, 15, 6)
# k.spinRobot(-15, 15, 41)
# k.moveDistance(15, 15, 52)
k.LmediumMotorDegrees(100, 160)
k.LmediumMotorDegrees(100, -160)
k.LmediumMotorDegrees(100, 160)
k.LmediumMotorDegrees(100, -160)
k.LmediumMotorDegrees(100, 160)
k.LmediumMotorDegrees(100, -160)