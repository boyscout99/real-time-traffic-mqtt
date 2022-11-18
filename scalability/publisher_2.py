#publisher
from datetime import datetime
import paho.mqtt.client as mqtt
import json
import io
import os
import time


client = mqtt.Client()
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
	print("timestamp = ", timestamp)
	current_time = "TRAFFIC JAM ON " + str(datetime.fromtimestamp(timestamp)) + '\n'
	print("Published ", current_time, '\n')
	return timestamp, data


if __name__ == '__main__':
	# Connect to localhost
	client.connect('localhost', 1884)
	TOPIC = input("Enter the topic: ")
	print("Publishing data on topic ", TOPIC, "\n---------------------------")
	# client.publish('traffic', input("Message : "))
	# Parse all the files containing traffic information
	for file in sorted(os.listdir(directory)):
		timestamp, data = read_data(file, path)
		publish_data(timestamp, data)
		# Wait to update traffic information (about 50", here 2" for testing purposes)
		time.sleep(2)
