#!/usr/bin/env micropython
from Kronos import Kronos
from time import sleep
from ev3dev2.motor import SpeedPercent
k = Kronos()

def run3():
    k.moveDistance(30, 30, 6)
    k.spinRobot(10, -10, 40)
    k.moveDistance(30, 30, 7)
    k.spinRobot(-10, 10, 40)
    k.moveDistance(45, 45, 51)
    k.RmediumMotorDegrees(5, -100)
    k.moveDistance(15, 15, -1)
    k.LmediumMotorDegrees(30, 120)
    k.LmediumMotorDegrees(100, -120)
    k.LmediumMotorDegrees(30, 130)
    k.LmediumMotorDegrees(100, -130)
    k.LmediumMotorDegrees(30, 130)
    k.LmediumMotorDegrees(100, -130)
    k.RmediumMotorDegrees(30, 145, block=False)
    k.moveDistance(15, 15, -5, False)
    k.moveDistance(40, 40, -15, False)
    k.spinRobot(10, -10, 45)
    k.moveDistance(70, 70, -40, False)
    k.spinRobot(0, -30, 60)