clients = []


class Object(object):
    pass

class mapping:
    door = Object()
    lock = Object()
    door.out1 = 10
    door.out2 = 9
    door.in1 = 11
    lock.out1 = 22 #auf
    lock.out2 = 23 #zu
    lock.in1 = 24 #auf
    lock.in2 = 25 #zu

class state:
    state = 5
    stateName = ['locked',
                'rw_opening',
                'rw_unlocked',
                'safe_door_opening',
                'unlocked',
                'init']
