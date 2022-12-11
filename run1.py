#!/usr/bin/env micropython

def run1():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
    from time import sleep
    from ev3dev2.motor import MoveDifferential, OUTPUT_A, OUTPUT_D
    from ev3dev2.wheel import EV3EducationSetTire
    from ev3dev2.button import Button
    from ev3dev2.sound import Sound
    from commonFunctions import runParallel
    from ev3dev2.console import Console

    odom = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3EducationSetTire, 116)
    k = Kronos()
    btn = Button()
    snd = Sound()
    scr = Console()
    

    # try:
    k.moveDistance(50.5, 50, 40)
    # 60, 60
    k.moveDistance(15, 15, 9)
    k.moveDistance(20, 20, -3)
    k.spinRobot(-15, 15, 38)
#only changed by 2 deg to ensure the middle sensor catches the black line

    k.moveUntilColorlt(35, 35, INPUT_2, 16)
    k.moveUntilColorlt(0, 15, INPUT_4, 16)
    k.moveDistance(20, 20, 7)
    k.spinRobot(0, -30, 170)
# #starting to do windmill

    k.moveDistance(40, 40, 13)
    sleep(0.5)
    k.moveDistance(-30, -30, 5)
    k.spinRobot(5, -5, 2)
    sleep(0.25)
    k.moveDistance(30, 30, 8)
    sleep(0.5)
    k.moveDistance(-30, -30, 6)
    sleep(0.25)
    k.moveDistance(30, 30, 9)

    k.moveDistance(-20, -20, 8)
    
    k.spinRobot(15, -15, 10)
    k.moveDistance(-15, -15, 4)
    
    k.LmediumMotorDegrees(100, 2700)
    k.moveDistance(-100, -96, 19)
    sleep(2)
    k.moveDistance(15, 15, 10)
    k.moveDistance(-100, -100, 10)
    # 100, 99
    sleep(1)

    k.LmediumMotorDegrees(-100, 2700, block=False)
    k.spinRobot(0, 30, 190)
    # 150
    k.moveDistance(20, 20, 1, brake=False)
    k.moveDistance(-85, -100, 90)