#!/usr/bin/env micropython
from Kronos import *
import math
from ev3dev2.sensor import *
from ev3dev2.sound import *
from ev3dev2.console import *
from ev3dev2.motor import *

k = Kronos()
scr = Console()
o = k.mdiff

o.odometry_start(0)
o.on_to_coordinates(15, 100, 100)
o.odometry_stop()