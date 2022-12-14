#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from time import sleep
from ev3dev2.motor import SpeedPercent

k = Kronos()

def run4():
    if 1==1:
        k.moveDistance(35, 35, 25)
        k.lfLTime(15, True, 2)
        k.moveUntilColorlteq( 20, 20, port=INPUT_1, RLI=12)
        k.moveUntilColorlt(50, 50, INPUT_4, 12)
        k.moveDistance(15, 15, 2)

        k.spinRobot(left_power=15,right_power=-15, degrees=45)
        k.moveDistance(35, 35, 16)
        k.spinRobot(left_power=15,right_power=-15, degrees=63)
            
        #adjust to the sweet spot for distance for both the units and the water units 

        k.moveDistance(40, 40, 8)
        k.spinRobot(40, 0, 28)

        #k.moveDistance(-15, 15, 1)
        k.RmediumMotorDegrees(-85, 1400)
        # 1400
        #water barrel drop in circle
        k.moveDistance(speedL=30, speedR=30, distanceCM=22)
        k.spinRobot( left_power=15, right_power=-15, degrees=20)
        k.moveDistance(speedL=-30, speedR=-30, distanceCM=5)

        k.LmediumMotorDegrees(speed=10, degrees=100)
        k.LmediumMotorDegrees(speed=10, degrees=150, block=False)
        # move arm up x # of degrees
        # turn clockwise to straighten about 25)
        k.spinRobot( left_power=20, right_power=-20, degrees=15)
        # reverse to black
        # square to black
        k.LmediumMotorDegrees(speed=-100, degrees=20, block=False)
        k.moveDistance(-15, -15, 3)
        k.squareToBlack( power=-20, sensor1=INPUT_1, sensor2=INPUT_4)
        # reverse x distance, 
        # move up arm up slightly, 
        k.moveDistance(-60, -60, 12)

        k.moveDistance(20, 20, 3)
        k.squareToBlack(20, INPUT_1, INPUT_4)
        k.moveDistance(15, 15, 8)
        k.moveUntilColorlt(-20, 20, INPUT_1, 12)
        
        k.lfLColorRangeR(15, True, 0, 12)
        k.squareToRange(5, 80, 100, INPUT_2, INPUT_4)
        k.LmediumMotorDegrees(speed=-100, degrees=210)
        k.mmL.on_for_seconds(SpeedPercent(-10), 0.5)
        
        k.moveDistance(40, 40, 16)

        k.moveUntilColorgt(0, 15, INPUT_2, 80)
        k.moveUntilColorlt(0, 15, INPUT_2, 16)
        k.moveDistance(20, 20, 5)
        k.LmediumMotorDegrees(85, 240)
        k.RmediumMotorDegrees(100, 90)
        k.moveDistance(-15, -15, 2)

        k.spinRobot(40, -40, 65)
        # 75

    k.squareToBlack(20, INPUT_1, INPUT_4)

    k.moveDistance(35, 35, 31)
    # k.RmediumMotorDegrees(-100, 800)
   # k.moveDistance(35, 35, 11)

    k.spinRobot(-35, 35, 105)
    k.moveDistance(35, 35, 17)