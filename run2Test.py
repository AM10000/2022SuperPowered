#!/usr/bin/env micropython
from Kronos import Kronos
from time import sleep
from ev3dev2.motor import MoveTank
from ev3dev2.sensor import *
k= Kronos()
 
k.moveDistance(45, 71)
k.lfLColorRangeR(20, True, 45, 47,)
k.LmediumMotorDegrees(35, 40)
k.spinRobot(20,-20,30)
k.moveDistance(30, 40)