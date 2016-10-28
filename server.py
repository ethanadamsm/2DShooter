import PodSixNet, time
from time import sleep
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server

from time import sleep

class ClientChannel(Channel):
	def Network(self, data):
		print data

class GameServer(Server):
	channelClass = ClientChannel

	def __init__(self, *args, **kwargs):
		Server.__init__(self, *args, **kwargs)

	def Connected(self, channel, addr):
		channels.append(channel)
		channel.Send({"message": "hello"})

print "Starting server on localhost"
gameser = GameServer(localaddr = ('localhost', 1337))
while True:
	gameser.Pump()
	sleep(.01)