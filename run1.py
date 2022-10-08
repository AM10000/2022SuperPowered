#!/usr/bin/env micropython
def run1():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
    from time import sleep
    from ev3dev2.motor import MoveDifferential, OUTPUT_A, OUTPUT_D
    from ev3dev2.wheel import EV3EducationSetTire


    odom = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3EducationSetTire, 116)
    k = Kronos()
    # k.moveDistance(35, 35, 45)
    # k.moveDistance(15, 15, 8)
    #Watch television mission finished

    # try:
    '''
    k.moveDistance(20, 20, -6)
    k.spinRobot(-15, 15, 40)
    k.moveUntilColorlt(30, 30, INPUT_2, 16)
    k.moveUntilColorlt(0, 15, INPUT_4, 16)
    k.moveDistance(15, 15, 4)
    k.spinRobot(15, -15, 82)
    # k.moveUntilColorlt(15, 0, INPUT_1, 13)
    # k.moveUntilColorlt(0, 10, INPUT_4, 13)
    # k.spinRobot(0, 5, 10)
    #Aligned to turbine mission
    k.moveDistance(30, 30, 12)
    sleep(1)
    k.moveDistance(-30, -30, 4)
    k.spinRobot(-5, 5, 2)
    sleep(0.5)
    k.moveDistance(30, 30, 6)
    sleep(0.75)
    k.moveDistance(-30, -30, 4)
    sleep(0.75)
    k.moveDistance(30, 30, 7)
    k.moveDistance(-15, -15, 2)
    # k.squareToBlack(-10, INPUT_2, INPUT_4)
    '''
    k.moveDistance(-30, -30, 10)
    k.LmediumMotorDegrees(100, 2300)
    k.moveDistance(-100, -100, 18)
        # k.spinRobot(-15, 15, 165)
        # k.moveDistance(25, 25, 15)
        # k.squareToRange(10, 0, 25, INPUT_1, INPUT_2)
        # err = k.error(20, 90, odom)
        # if err == True:
        #     k.spinRobot(15, -15, 20)
        #     k.moveDistance(-50, -50, 51)
        # else:
        #     k.moveDistance(-15, -15, 10)
        #     k.LmediumMotorDegrees(100, 2500)
        #     k.moveDistance(15, 15, 13)
        #     k.moveDistance(-30, -30, 2)
        #     k.spinRobot(-30, 30, 80)
        #     k.moveDistance(100, 100, 90)