#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from time import sleep
from ev3dev2.motor import SpeedPercent

k = Kronos()

def run4():
    mission = '1.5'
    k.moveDistance(25, 25, 25)
    k.lfLTime(15, True, 2)
    k.moveUntilColorlteq( 20, 20, port=INPUT_1, RLI=12)
    k.moveUntilColorlt(50, 50, INPUT_4, 12)
    k.moveDistance(15, 15, 2)

    k.spinRobot(left_power=15,right_power=-15, degrees=45)
    k.moveDistance(30, 30, 16)
    k.spinRobot(left_power=15,right_power=-15, degrees=63)

    if mission == '1.5':
        #adjust to the sweet spot for distance for both the units and the water units 
    
        #new attachment
        k.moveDistance(30, 30, 5)

        #old attachment
        #k.moveDistance(40, 40, 8)

        k.spinRobot(40, 0, 30)
    
    if mission == '2' or mission == '0' or mission == '...2' or mission == '...3' or mission == '...4' or mission == '...4.5' or mission == '...5' or mission == '...6':
        k.RmediumMotorDegrees(-85, 1500)
        #water barrel drop in circle
        k.moveDistance(speedL=30, speedR=30, distanceCM=20)
        k.spinRobot( left_power=15, right_power=-15, degrees=20)
        k.moveDistance(speedL=-30, speedR=-30, distanceCM=5)
    if mission == '3' or mission == '0' or mission == '...3' or mission == '...4' or mission == '...4.5' or mission == '...5' or mission == '...6':
        k.LmediumMotorDegrees(speed=10, degrees=100)
        k.LmediumMotorDegrees(speed=10, degrees=150, block=False)
        # move arm up x # of degrees
        # turn clockwise to straighten about 25)
        k.spinRobot( left_power=20, right_power=-20, degrees=10)
    if mission == '4' or mission == '0' or mission == '...4' or mission == '...4.5' or mission == '...5' or mission == '...6':
        # reverse to black
        # square to black
        k.LmediumMotorDegrees(speed=-100, degrees=30, block=False)
        k.squareToRange(-20, 80, 200, INPUT_2, INPUT_4)
        k.squareToBlack( power=-20, sensor1=INPUT_2, sensor2=INPUT_4)
        # reverse x distance, 
        # move up arm up slightly, 
        k.moveDistance(-40, -40, 12)
    if mission == '4.5' or mission == '0' or mission == '...4.5' or mission == '...5' or mission == '...6':
        k.moveDistance(20, 20, 3)
        k.squareToBlack(20, INPUT_1, INPUT_4)
        k.moveDistance(15, 15, 8)
        k.moveUntilColorlt(-20, 20, INPUT_1, 12)
        
        k.lfLColorRangeR(15, True, 0, 12)
        k.squareToRange(5, 80, 100, INPUT_2, INPUT_4)
        k.LmediumMotorDegrees(speed=-100, degrees=210)
        k.moveDistance(40, 40, 16)
    if mission == '5' or mission == '0' or mission == '...5' or mission == '...6':
        k.moveUntilColorgt(0, 15, INPUT_2, 80)
        k.moveUntilColorlt(0, 15, INPUT_2, 16)
        k.moveDistance(20, 20, 3)
        k.LmediumMotorDegrees(70, 210)
        k.mmL.on_for_seconds(SpeedPercent(100), 0.5)
    if mission == '6' or mission == '0':
        k.spinRobot(40, -40, 60)
        k.squareToBlack(20, INPUT_1, INPUT_4)
        k.moveDistance(35, 35, 29)
        k.spinRobot(-35, 35, 110)
        k.moveDistance(35, 35, 14)
