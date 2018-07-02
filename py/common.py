# from __main__ import threading
import threading

clients = []

unlock = threading.Event()

openDuration = 1.0
rampDuration = 0.5
vmax = 100
vclose = 70


class Object(object):
    pass

class mapping:
    door = Object()
    lock = Object()
    ledBody = Object()
    ledEdge = Object()
    ledInner = Object()
    door.out1 = 10 #zu
    door.out2 = 9 #auf
    door.in1 = 11 #zu
    lock.out1 = 22 #auf
    lock.out2 = 23 #zu
    lock.in1 = 24 #auf
    lock.in2 = 25 #zu
    ledBody.r = 17
    ledBody.g = 18
    ledBody.b = 27
    ledEdge.r = 5
    ledEdge.g = 6
    ledEdge.b = 13
    ledInner.w = 19

class state:
    stateName = [
    'locked',           #0
    'rw_opening',       #1
    'rw_closing',       #2
    'rw_unlocked',      #3
    'safe_door_opening',#4
    'safe_door_closing',#5
    'unlocked',         #6
    'init'              #7
    ]
    state = stateName.index('init')
