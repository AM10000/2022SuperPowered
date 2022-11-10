#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from time import sleep

k = Kronos()

def run4():

    k.moveDistance(30, 30, 25)
    k.lfLTime(15, True, 2)
    k.moveUntilColorlteq( 20, 20, port=INPUT_1, RLI=12)
    # k.moveUntilColorgteq( 30, 20, port=INPUT_1, RLI=80)
    k.moveUntilColorlt(50, 50, INPUT_4, 12)
    k.moveDistance(15, 15, 2)
    k.spinRobot(left_power=15,right_power=-15, degrees=45)
    k.moveDistance(30, 30, 16)
    k.spinRobot(left_power=15,right_power=-15, degrees=63)
    #adjust to the sweet spot for distance for both the units and the water units 
    
    k.moveDistance(40, 40, 8)
    k.spinRobot(40, 0, 30)
    k.RmediumMotorDegrees(-85, 1200)
    #water barrel drop in circle
    k.moveDistance(speedL=30, speedR=30, distanceCM=20)
    k.spinRobot( left_power=15, right_power=-15, degrees=20)
    k.moveDistance(speedL=-30, speedR=-30, distanceCM=5)
    k.LmediumMotorDegrees(speed=10, degrees=100)
    k.LmediumMotorDegrees(speed=10, degrees=150, block=False)
    # move arm up x # of degrees
    # turn clockwise to straighten about 25)
    k.spinRobot( left_power=20, right_power=-20, degrees=15)
    # reverse to black
    # square to black
    k.LmediumMotorDegrees(speed=-100, degrees=40, block=False)
    k.squareToBlack( power=-20, sensor1=INPUT_2, sensor2=INPUT_4)
    # reverse x distance, 
    # move up arm up slightly, 
    k.moveDistance(-40, -40, 12)
    k.moveDistance(30, 30, 20)
    k.moveUntilColorlt(-30, 0, INPUT_1, 12)
    k.RmediumMotorDegrees(-100, 2000, block=False)
    k.lfLColorRangeR(15, True, 0, 12)
    # k.moveUntilColorgt(0, 10, INPUT_4, 80)
    k.spinRobot(0, 20, 50)
    k.moveDistance(100, 100, distanceCM=30)
    # reverse further
    # disengage from the mission ( reverse)

    # k.moveDistance(speedL=100,speedR=100,distanceCM=30)
    # k.spinRobot(left_power=0, right_power=30,degrees=120)
    # k.moveDistance(speedL=100,speedR=90,distanceCM=100)
    #speed up 
