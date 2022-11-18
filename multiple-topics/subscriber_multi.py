# subscriber
import paho.mqtt.client as mqtt
from datetime import datetime
import time
import sqlite3

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
	print("Connected to a broker!")
	client.subscribe(TOPIC)
	print("Subscribed to the topic ", TOPIC)

def on_message(client, userdata, message):
	# print(message.payload.decode('utf-8'))
	data = message.payload.decode('utf-8')
	# print('Received TRAFFIC UPDATE AT ')
	# Save data on the database
	db_conn = userdata['db_conn']
	sql = 'INSERT INTO traffic_data (data) VALUES (?)'
	cursor = db_conn.cursor()
	cursor.execute(sql, [data])
	db_conn.commit()
	cursor.close()

def on_log(client, userdata, level, buf):
    print("client: ", client._client_id, " log: ", buf)

if __name__ == '__main__':

	client_name = input("Enter client name: ")
	client = mqtt.Client(client_name)
	# Connect to the database
	DATABASE_FILE = "traffic_data_client_"+client._client_id.decode('utf_8')+".db"
	db_conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
	sql = """
	CREATE TABLE IF NOT EXISTS traffic_data (
		data TEXT NOT NULL
	) 
	"""
	cursor = db_conn.cursor()
	cursor.execute(sql)
	cursor.close()

	topic1 = input("Enter topic 1 to subscribe: ")
	topic2 = input("Enter topic 2 to subscribe: ")
	TOPIC = [(topic1, 0),(topic2, 0)]
	option = input("Enter option (sub/unsub): ")

	client.user_data_set({'db_conn': db_conn})
	client.on_connect = on_connect
	client.on_message = on_message
	client.on_log = on_log
	client.connect('localhost', 1883)

	if option == 'unsub':

		client.loop_start()
		print('Waiting for 10 seconds before unsubscribing...')
		time.sleep(10)
		client.unsubscribe(TOPIC)
		print('***\nUnsubscribed\n***')
		time.sleep(2)
		client.loop_stop()
		client.disconnect()

	elif option == 'sub':

		client.loop_start()
		time.sleep(60)
		client.loop_stop()
		client.disconnect()
	else:
		print('Wrong command. Exiting...')
		client.disconnect()
		
	
		
	t_sub.close()
