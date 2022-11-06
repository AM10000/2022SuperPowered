#!/usr/bin/env micropython
from Kronos import *
import math
from ev3dev2.sensor import *
from ev3dev2.sound import *
from ev3dev2.console import *
from ev3dev2.motor import *

k = Kronos()
scr = Console()

#positive degrees is down
k.mmR.on_for_seconds(SpeedPercent(-5), 2, block=False)