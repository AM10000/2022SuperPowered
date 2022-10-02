#!/usr/bin/env micropython
# 2022SuperPowered
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
from ev3dev2.motor import SpeedPercent
from time import sleep

k=Kronos()
# k.mdiff.odometry_start()
k.moveDistance(15, 15, 20)
k.spinRobot(-15, 15, 32)
k.moveDistance(30, 30, 44)
# k.mdiff.on_to_coordinates(SpeedPercent(30), -220, 600)
k.moveUntilColorgteq(left_power=10, right_power=10, port=INPUT_4, RLI=80)
k.moveUntilColorlteq(left_power=-15, right_power=15, port=INPUT_4, RLI=12)
k.moveDistance(-15, -15, 7)
k.spinRobot(-15, 15, 12)
k.squareToBlack(15, INPUT_1, INPUT_4)
k.moveDistance(15, 15, 16)
k.RmediumMotorDegrees(30, 350)
sleep(0.5)
k.RmediumMotorDegrees(-90, 350)