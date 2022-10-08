#!/usr/bin/env micropython
def run2():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_2, INPUT_4
    k= Kronos()

    
    k.RmediumMotorDegrees(-5, 140, block=False)
    k.moveDistance(45, 45, 78)
    k.lfLTime(10, False, 1.5, 2.3)
    k.squareToRange(15, 0, 16, INPUT_2, INPUT_4)
    k.LmediumMotorDegrees(-100, 200)
    k.squareToRange(15, 80, 100, INPUT_2, INPUT_4)
    
    k.moveDistance(70, 70, 100, brake=False)
   # k.moveDistance(20, 20, 25, brake=False)
   #k.moveDistance(50, 50, 45, brake=False)