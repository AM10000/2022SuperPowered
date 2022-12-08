#!/usr/bin/env micropython
def run3():
    from Kronos import Kronos
    from time import sleep
    from ev3dev2.motor import SpeedPercent
    k = Kronos()

    k.moveDistance(40, 40, 62)
    k.RmediumMotorDegrees(5, -100)
    k.moveDistance(5, 5, -1)
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

