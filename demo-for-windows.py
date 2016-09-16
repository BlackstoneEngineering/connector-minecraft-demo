from mc import *
import mbed_connector_api as mdc 
from base64 import standard_b64decode as b64decode
import math
import time

ep = "YOUR ENDPOINT NAME"
buttonID = '/3200/0/5501'
led = '/3201/0/5850'

x = mdc.connector("YOUR API KEY")
x.startLongPolling()
mc = Minecraft()
x_ = y_ = z_ = 0

def notificationHandler(data):
	global x_, y_, z_
	mc.postToChat("Notification Received! Have some DIAMOND_ORE!!")
	playerPos = mc.player.getPos()
	x_ = math.ceil(playerPos.x+1)
	y_ = math.ceil(playerPos.y+1)
	z_ = math.ceil(playerPos.z+1)
	mc.postToChat(str(x_)+","+str(y_)+","+str(z_))
	mc.setBlock(x_,y_,z_,56)

e = x.putResourceSubscription(ep,buttonID)
while not e.isDone():
	None
if e.error:
	mc.postToChat("ERROR in subscribing to Resource: ",e.error.errType, e.error.error)
else:
	mc.postToChat("Subscribed Sucessfully!")

x.setHandler('notifications',notificationHandler)

while True:
	hits = mc.events.pollBlockHits()
	if hits:
		for thing in hits:
			mc.postToChat(str(math.ceil(thing.pos.x))+","+str(math.ceil(thing.pos.y))+","+str(math.ceil(thing.pos.z))+" ?= "+str(x_)+","+str(y_)+","+str(z_))
			if math.ceil(thing.pos.x)==x_ and math.ceil(thing.pos.y) == y_ and math.ceil(thing.pos.z) == z_:
				mc.postToChat("Posting to endpoint!")
				x.postResource(ep,led)
	time.sleep(1)

