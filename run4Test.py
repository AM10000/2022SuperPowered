#!/usr/bin/env micropython
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4

k = Kronos()

k.moveDistance(30, 30, 25)
k.lfLTime(15, True, 2)
k.moveUntilColorlteq( 20, 20, port=INPUT_1, RLI=12)
k.moveUntilColorgteq( 30, 20, port=INPUT_1, RLI=80)
k.moveUntilColorlt(50, 50, INPUT_4, 12)
k.moveDistance(15, 15, 2)
k.spinRobot(left_power=15,right_power=-15, degrees=45)
k.moveDistance(30, 30, 16)


#start of high five shared mission 
k.spinRobot(left_power=15,right_power=-15, degrees=63)
#adjust to the sweet spot for distance for both the units and the water units 
k.moveDistance(40, 40, 8)
k.spinRobot(40, 0, 40)
#k.LmediumMotorDegrees(speed=15, degrees=180)
k.RmediumMotorDegrees(speed=-100, degrees=900)

k.spinRobot(40, 0, 40)
k.moveDistance(speedL=-10, speedR=-10, distanceCM=3, block=False)

k.LmediumMotorDegrees(speed=15, degrees=-180)
k.LmediumMotorDegrees(speed=10, degrees=-100)
k.LmediumMotorDegrees(speed=10, degrees=-100, block=False)
# k.moveDistance(speedL=50,speedR=50,distanceCM=35)
# k.spinRobot(left_power=0, right_power=30,degrees=160)
# k.moveDistance(speedL=100,speedR=100,distanceCM=100)
#speed up 
