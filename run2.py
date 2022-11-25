#!/usr/bin/env micropython
def run2():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_2, INPUT_4
    k= Kronos()

    
    k.RmediumMotorDegrees(-5, 140, block=False)
    k.moveDistance(55.5, 55, 78)
    k.lfLTime(10, False, 1.5, 2.3)
    k.squareToRange(10, 0, 16, INPUT_2, INPUT_4)
    k.moveDistance(5, 5, 1)
    k.LmediumMotorDegrees(-100, 210)
    k.squareToRange(10, 75, 200, INPUT_2, INPUT_4)
    
    k.moveDistance(70.8, 70, 60, brake=False)
    k.moveDistance(90, 100, 40, brake=False)