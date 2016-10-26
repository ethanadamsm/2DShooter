import PodSixNet.Channel
import PodSixNet.Server
from time import sleep
channels = []
class ClientChannel(PodSixNet.Channel.Channel):
	def Network(self, data):
		print data

class GameServer(PodSixNet.Server.Server):
	channelClass = ClientChannel

	def Connected(self, channel, addr):
		channels.append(channel)
		channel.Send({"message": "hello"})

print "Starting server on localhost"
gameser = GameServer()
while True:
	gameser.Pump()
	sleep(.01)
	for channel in channels:
		channel.Send({"message": "hello"})
		print channel