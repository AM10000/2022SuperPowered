#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import *
from time import sleep
from ev3dev2.motor import MoveTank
k = Kronos()
k.moveDistance(30, 50)
k.moveDistance(15, 7)
#Watch television mission finished
k.moveDistance(15, -11)
k.spinRobot(-15, 15, 50)
k.moveUntilColorlt(30, 30, INPUT_4, 12)
k.moveUntilColorgt(15, 0, INPUT_1, 80)
k.moveUntilColorlt(15, 0, INPUT_1, 12)
k.moveUntilColorlt(0, 15, INPUT_4, 12)
#Aligned to turbine mission
k.moveDistance(30, 8)
sleep(1)
k.moveDistance(-30, 4)
k.spinRobot(5, -5, 2)
sleep(0.5)
k.moveDistance(30, 6)
sleep(1)
k.moveDistance(-30, 4)
k.spinRobot(5, -5, 4)
sleep(0.5)
k.moveDistance(30, 7)
k.squareToBlack(-15, INPUT_4, INPUT_2)
k.moveDistance(-15, 7)
k.spinRobot(-15, 15, 180)
k.squareToRange(5, 0, 20)