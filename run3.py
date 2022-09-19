#!/usr/bin/env micropython
def run3():
    from Kronos import Kronos
    from time import sleep
    k = Kronos()

    k.moveDistance(40, 40, 61)
    k.RmediumMotorDegrees(5, -170, block=False)
    k.LmediumMotorDegrees(20, 120)
    k.LmediumMotorDegrees(20, -120)
    k.LmediumMotorDegrees(20, 130)
    k.LmediumMotorDegrees(20, -130)
    k.LmediumMotorDegrees(20, 130)
    k.LmediumMotorDegrees(20, -130)
    sleep(1)
    k.RmediumMotorDegrees(20, 170,block=False)
    k.moveDistance(15, 15, -20)
    k.spinRobot(15, -15, 45)
    k.moveDistance(70, 70, -40)

