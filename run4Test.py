#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4

k = Kronos()
k.moveDistance(30, 30, 20)
k.lfLTime(15, True, 2)
k.moveUntilColorlt(40, 40, INPUT_4, 12)
k.moveDistance(15, 15, 2)
k.spinRobot(left_power=15,right_power=-15, degrees=45)
k.moveDistance(30, 30, 15)
k.moveDistance(30, 30, 12)
k.RmediumMotorDegrees(speed=40, degrees=70)
#start of high five shared mission 
k.spinRobot(left_power=15,right_power=-15, degrees=70)
k.moveDistance(40, 40, 25)
k.spinRobot(15, 0, 60)
k.moveDistance(speedL=-10, speedR=-10, distanceCM=3, block=False)
k.LmediumMotorDegrees(speed=-10, degrees=100)
k.LmediumMotorDegrees(speed=-10, degrees=100, block=False)
k.moveDistance(speedL=50,speedR=50,distanceCM=35)
k.spinRobot(left_power=0, right_power=30,degrees=160)
k.moveDistance(speedL=100,speedR=100,distanceCM=100)
#speed up 
