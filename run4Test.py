#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4

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


    #start of high five shared mission 
    k.spinRobot(left_power=15,right_power=-15, degrees=63)
    #adjust to the sweet spot for distance for both the units and the water units 
    k.moveDistance(40, 40, 8)
    k.spinRobot(40, 0, 30)
    k.RmediumMotorDegrees(speed=-85, degrees=1200)
    k.moveDistance(speedL=30, speedR=30, distanceCM=20)
    k.LmediumMotorDegrees(speed=8, degrees=210)
    k.moveDistance(-3, -3, -3, block=False)
    k.moveDistance(speedL=100,speedR=100,distanceCM=30)
    k.spinRobot(left_power=0, right_power=30,degrees=60)
    k.moveDistance(speedL=100,speedR=90,distanceCM=100)
    #speed up 
