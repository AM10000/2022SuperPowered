#!/usr/bin/env micropython
def run2():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_2, INPUT_4
    k= Kronos()

    
    
    k.moveDistance(75.8, 75, 78)
    # 75.5
    k.RmediumMotorDegrees(-100, 140, block=False)
    k.lfLTime(10, False, 1.5, 2.3)
    k.squareToRange(10, 0, 16, INPUT_2, INPUT_4)
    k.moveDistance(5, 5, 1)
    k.LmediumMotorDegrees(-100, 210)
    k.squareToRange(10, 75, 200, INPUT_2, INPUT_4)
    
    k.moveDistance(72, 70, 70, brake=False)
    # 70.8
    k.moveDistance(70, 100, 30, brake=False)