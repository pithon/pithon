import sys
sys.path.append("..")

from core2 import World
import Pyro4
import thread
import WorldHandler

ip_address=raw_input("IP Address>> ")
port=int(raw_input("Port>> "))

print "Starting server..."
print "Loading daemon..."
daemon=Pyro4.Daemon(ip_address, port)
#print "Locating nameserver..."
#nameserver=Pyro4.locateNS()
print "Loading world..."
world=World.World()
print "Setting up daemon..."
#nameserver.register("game", daemon.register(world))
print "(Pyro ID: "+str(daemon.register(world, "WORLD"))+")"
print "Starting world thread..."
thread.start_new_thread(WorldHandler.handle_world, (world,))
print "Starting daemon..."
daemon.requestLoop()
