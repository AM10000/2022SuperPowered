#!/usr/bin/env micropython
def run3():
    from Kronos import Kronos
    from time import sleep
    from ev3dev2.motor import SpeedPercent
    k = Kronos()

    k.moveDistance(40, 40, 62)
    k.RmediumMotorDegrees(5, -100)
    k.moveDistance(5, 5, -1)
    k.LmediumMotorDegrees(20, 120)
    k.LmediumMotorDegrees(20, -120)
    k.LmediumMotorDegrees(20, 130)
    k.LmediumMotorDegrees(20, -130)
    k.LmediumMotorDegrees(20, 130)
    k.LmediumMotorDegrees(20, -130)
    sleep(1)
    k.RmediumMotorDegrees(20, 145, block=False)
    k.moveDistance(15, 15, -20)
    k.spinRobot(10, -10, 45)
    k.moveDistance(70, 70, -40, False)
    k.spinRobot(0, -10, 60)

