#!/usr/bin/env micropython
# 2022SuperPowered
from Kronos import Kronos
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2


k=Kronos()
k.moveDistance(15, 15, 35)
k.moveUntilColorgteq(left_power=20, right_power=20, port=INPUT_4, RLI=80)
k.moveUntilColorlteq(left_power=-15, right_power=15, port=INPUT_4, RLI=12)
