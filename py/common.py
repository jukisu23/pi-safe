import threading

dbfile = "/var/www/db/misafe.db"
clients = []
globalrgb = {}

opened = threading.Event()
unlocked = threading.Event()


class colors:
    blinkWrong = {"r": 255, "g": 0, "b": 0}
    colorOpen = {"r": 0, "g": 255, "b": 0}
    blinkCount = 5
    blinkSpeed = 1 # in sec
    blinkWhich = 1
    colorTrigger = threading.Event()
    colorEvent = None
    colorEventArgs = None

lockDuration = 3
openDuration = 9.0
rampDuration = 0.5
vmax = 50
vclose = 50

class Object(object):
    pass

class mapping:
    door = Object()
    lock = Object()
    ledBody = Object()
    ledEdge = Object()
    ledInner = Object()
    motion_detector = Object()
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
    ledInner.w = 20
    motion_detector.in1 = 21

class state:
    stateName = [
    'locked',           #0
    'rw_opening',       #1
    'rw_closing',       #2
    'rw_unlocked',      #3
    'safe_door_opening',#4
    'safe_door_closing',#5
    'unlocked',         #6
    'init',             #7
    'open',             #8
    'timeout'           #9
    ]
    state = stateName.index('init')
