#!/usr/bin/env micropython


def run1():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
    from time import sleep
    from ev3dev2.motor import MoveDifferential, OUTPUT_A, OUTPUT_D
    from ev3dev2.wheel import EV3EducationSetTire


    odom = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3EducationSetTire, 116)
    k = Kronos()
    
    #Watch television mission finished

    # try:

    k.moveDistance(40, 40, 45)
    k.moveDistance(15, 15, 4)
    k.moveDistance(20, 20, -3)
    k.spinRobot(-15, 15, 38)
    #only changed by 2 deg to ensure the middle sensor catches the black line
    k.moveUntilColorlt(30, 30, INPUT_2, 16)
    k.moveUntilColorlt(0, 15, INPUT_4, 16)
    k.moveDistance(15, 15, 5)
    k.spinRobot(15, -15, 85)
    #starting to do windmill
    k.moveDistance(40, 40, 9)
    sleep(1)
    k.moveDistance(-30, -30, 5)
    k.spinRobot(5, -5, 2)
    sleep(0.5)
    k.moveDistance(30, 30, 8)
    sleep(0.75)
    k.moveDistance(-30, -30, 6)
    sleep(0.75)
    k.moveDistance(30, 30, 9)

    k.moveDistance(speedL=-50, speedR=-50, distanceCM=12)

    k.LmediumMotorDegrees(100, 2700)
    #2700
    k.moveDistance(-100, -100, 19)
    sleep(2)
    k.LmediumMotorDegrees(-100, 2700, block=False)

     
    k.spinRobot(0, 30, 150)
    k.moveDistance(-85, -100, 90)
    

    
       