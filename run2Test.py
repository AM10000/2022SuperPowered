#!/usr/bin/env micropython
from Kronos import Kronos
from time import sleep
from ev3dev2.motor import MoveTank
from ev3dev2.sensor import *
k= Kronos()

k.moveDistance(45, 71)
k.moveUntilColorlt(20, 20, 1, 47)
k.LmediumMotorDegrees(35, 40)
#done with power plant
k.spinRobot(20,-20,30)
k.moveDistance(30, 40)
#done with hydroelectric dam and collected looped water
k.spinRobot(-20, 20, -30)
k.moveDistance(45, 30)