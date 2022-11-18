
# subscriber
import paho.mqtt.client as mqtt
import time

# client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
	print("Connected to a broker!")
	client.subscribe(TOPIC)
	print("Subscribed to the topic " + TOPIC)

def on_message(client, userdata, message):
	# print(message.payload.decode('utf-8'))
	data = message.payload.decode('utf-8')
	print('Received TRAFFIC UPDATE AT ')

def on_log(client, userdata, level, buf):
	print("client: ", client._client_id, " log: ", buf)

if __name__ == '__main__':

	#TOPIC = input("Enter topic to subscribe: ")
	TOPIC = 'traffic'
	# create and connect 20 clients
	clients=[]
	nclients=400
	mqtt.Client.connected_flag=False
	flag = True
	#create clients
	# half of them connected to one broker on port 1883
	for i  in range(1,int(nclients/2)):
		cname = "Client"+str(i)
		client = mqtt.Client(cname)
		clients.append(client)
		client.on_connect = on_connect
		client.on_message = on_message
		client.on_log = on_log
		client.connect('localhost', 1883)
	# half of them connected to the other broker on port 1884
	for i  in range(int(nclients/2)+1,nclients):
		cname = "Client"+str(i)
		client = mqtt.Client(cname)
		clients.append(client)
		client.on_connect = on_connect
		client.on_message = on_message
		client.on_log = on_log
		client.connect('localhost', 1884)
	print('Waiting to establish all connections ...')
	time.sleep(2)
	# Loop for each client
	while flag:
		for client in clients:
			# client.loop_start()
			client.loop(0.01)
			time.sleep(0.02)

	#time.sleep(60)
	for client in clients:
		# client.loop_stop()
		client.disconnect()
