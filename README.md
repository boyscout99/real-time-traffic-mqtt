# Part II: Pub/Sub Services using MQTT

## Running a Mosquitto MQTT message broker in Docker, 1 publisher and N subscribers

1. Pull the mosquitto image with `docker pull toke/mosquitto`
2. Run the image on ports 1883 and 9001 `docker run -ti -p 1883:1883 -p 9001:9001 toke/mosquitto` 
3. Run `python3 subscriber.py` on another terminal and type _traffic_ as topic and then _sub_ to subscribe option
4. Open another terminal and run `python3 publisher.py`, input _traffic_ as required topic
5. The clients now should receive the JSON data from the publisher

## Unsubscribe a client from one topic

1. Run again `python3 subscriber.py` with _traffic_ as topic but _unsub_ as second option
2. After some delay the client will automatically unsubscribe from the given topic and will no longer receive messages from the publisher

## Scalability analysis

### Case with 1 broker, 1 publisher and N subscribers

> NOTE! Use `ulimit -n 4096` to increase the maximum number of open files in the system

1. Run the broker on the Docker container
2. On another terminal run `python3 subscriber_scala.py`. This code will generate N subscribers which will connect to the same topic _traffic_
3. Open another terminal and run `python3 publisher_scala.py`. This publisher will automatically publish on _traffic_

### Case with 1 broker, M publishers and N subscribers

1.

### Case with 3 brokers, M publishers and N subscribers

1. 

## Using sqlite3 with Python, Sqlite Browser and MQTT Explorer

1. Run the mosquitto Docker container
2. Run the app `vehicle.py` 
3. Open the installed app MQTT Explorer with `mqtt-explorer`
4. Open the installed app Sqlite Browser with `sqlitebrowser` to see the file mqtt.db

------

## Resources

1. [Use shared volumes in Docker](https://docs.docker.com/storage/volumes/#share-data-among-machines)
2. [MQTT Protocol tutorial - LIVE DEMO using Mosquitto and CloudMQTT](https://www.youtube.com/watch?v=Oh3ZYAQBTko)
3. [Paho library on GitHub](https://github.com/eclipse/paho.mqtt.python)
4. [Paho library for Python](https://pypi.org/project/paho-mqtt/)
5. [sqlite3 Python library](https://docs.python.org/3/library/sqlite3.html)
6. [Docker and Mosquitto container on GitHub](https://github.com/toke/docker-mosquitto)
7. [Save MQTT data to sqlite database using Python](https://lindevs.com/save-mqtt-data-to-sqlite-database-using-python/)
