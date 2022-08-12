#!/usr/bin/env micropython

from ev3dev2.button import *
from ev3dev2.sound import *
from time import sleep
from ev3dev2.console import *
from Kronos import Kronos
from run1 import run1
from run2 import run2
from run3 import run3
from run4 import run4

def right():
    try:
        global run, snd
        snd.beep()
        if run < 4:
            run+=1
        elif run == 4:
            run = 1 
    except:
        print('RIGHT DID NOT WORK')
        sleep(5)
def left():
    try:
        global run, snd
        snd.beep()
        if run > 1:
            run-=1
        elif run==1:
            run = 4
    except:
        print('LEFT DID NOT WORK')
        sleep(5)
def enter():
    try:
        global run, snd, scr
        snd.beep()
        scr.text_at('>>>Run ' + str(run), 6, 3, True)
        if run==1:
            run1()
        elif run==2:
            run2()
        elif run==3:
            run3()
        elif run==4:
            run4()
        #globals()['run' + str(run)]()
    except Exception as e:
        print('Error-'+ str(run))
        print (e)
        #beep @ 500Hz for 2s
        snd.beep('-f 300 -l 2000')
        sleep(5)
try:
    try:
        b = Button()
        scr = Console()
        snd = Sound()
        try:
            k = Kronos()
        except:
            snd.beep('-f 600 -l 1000')
        finally:
            del k

    except:
        print('Init btn, scr, snd failed')
        sleep(5)

    run = 1
    snd.play_song((('D4', 'e3'),('D4', 'e3')))
    while True:
        scr.text_at('Run ' + str(run), 6, 3, True)
        sleep(0.1)
        if b.right == True:
            right()
        if b.left == True:
            left()
        if b.enter == True:
            enter()
            right()
except:
    print('Error in main')
    sleep(5)