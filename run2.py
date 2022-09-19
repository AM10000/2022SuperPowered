#!/usr/bin/env micropython
def run2():
    from Kronos import Kronos
    from ev3dev2.sensor import INPUT_2, INPUT_4
    k= Kronos()

    
    k.moveDistance(45, 45, 78)
    k.lfLTime(10, False, 1.5, 2.3)
    k.squareToRange(15, 0, 16, INPUT_2, INPUT_4)
    k.moveDistance(5, 5, 0)
    k.LmediumMotorDegrees(-80, 190)
    k.spinRobot(0, 15, 2)
    k.moveDistance(70, 70, 30)
    k.moveDistance(20, 20, 25, brake=False)
    k.moveDistance(50, 50, 45, brake=False)
    # k.spinRobot(-20, 20, 2.5)
    # k.lfLTime(20, True, 0.15)
    # k.LmediumMotorDegrees(70, 150)
    # #done with power plant
    # k.squareToRange(15, 80, 150, INPUT_2, INPUT_4)
    # # k.moveUntilColorlt(15, 0, INPUT_2, 12)