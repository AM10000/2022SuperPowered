#!/usr/bin/env micropython
from Kronos import Kronos
k = Kronos()

k.moveDistance(30, 50)
k.moveDistance(15, 7)
#Watch television mission finished
k.moveDistance(15, -11)
k.spinRobot(-15, 15, 50)
k.moveUntilColorlt(15, 15, )