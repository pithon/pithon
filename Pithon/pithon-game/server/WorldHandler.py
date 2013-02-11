import time

def handle_world(world):
    while 1:
        time.sleep(0.1)
        try:
            world.update_world()
        except BaseException as e:
            print "!!! AN UNEXPECTED ERROR WAS ENCOUNTERED IN THE TICK THREAD"
            print "!!! ERROR DUMP:"+str(e)