import PodSixNet.Channel

from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
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