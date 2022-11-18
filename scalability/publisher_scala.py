#publisher
from datetime import datetime
import paho.mqtt.client as mqtt
import os
import time


# client = mqtt.Client()
path = '/home/ringo/Downloads/sample_data_assignment2/'
directory = os.fsencode(path)

def publish_data(timestamp, data):
	# Publish given timestamps and JSON data
	# separator = '##########\n##########\n##########\n'
	# current_time = "TRAFFIC JAM ON " + str(datetime.fromtimestamp(timestamp)) + '\n'
	client.publish(TOPIC, data)
	return


def read_data(file, path):
	# Open and read data from all the files in the given directory
	filename = os.fsdecode(file)
	### Reading files
	json_file = open(path+filename, "r")
	# print(json_file.readable())
	data = json_file.read()
	json_file.close()
	timestamp = int(filename.replace('.json', ''))
	#print("timestamp = ", timestamp)
	current_time = "TRAFFIC JAM ON " + str(datetime.fromtimestamp(timestamp)) + '\n'
	print("Published ", current_time, '\n')
	return timestamp, data


if __name__ == '__main__':
	
	TOPIC = 'traffic'
		
	# create and connect 20 clients
	clients=[]
	nclients=20
	mqtt.Client.connected_flag=False
	flag = True
	#create publishers
	# half of them connected to broker on port 1883
	for i  in range(0,int(nclients/2)):
		cname = "Publisher"+str(i)
		client = mqtt.Client(cname)
		clients.append(client)
		client.connect('localhost', 1883)
	# other half connected to broker on port 1884
	for i  in range(int(nclients/2),nclients):
		cname = "Publisher"+str(i)
		client = mqtt.Client(cname)
		clients.append(client)
		client.connect('localhost', 1884)

	while flag:
		# Parse all the files containing traffic information
		for file in sorted(os.listdir(directory)):
			for client in clients:
				timestamp, data = read_data(file, path)
				publish_data(timestamp, data)
			
			# Wait to update traffic information (about 50", here 2" for testing purposes)
			time.sleep(2)
