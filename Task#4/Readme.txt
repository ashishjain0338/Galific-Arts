Instructions for running the kafka data pipeline and websocket
Prerequistes:-
Python Package: django ,simplejson , channels-redis
kafka server , redis server

Step 1: Running a kafka server(On Windows)
1)Download and install kafka.
2)Then cd to kafka bin and type the command :-> ".\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties"
3)Open a new cmd window and cd to kafka bin and type the command :-> ".\bin\windows\kafka-server-start.bat .\config\server.properties"
The third step would start the kafka server, To start kafka consumer:
4)Open a new cmd window and cd to kafka bin and type the command :-> ".\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic GalificData"

Step 2:Running the django server for websocket
1)cd to the galificdatapipeline directory and type the command "python manage.py runserver"

Step 3: Connecting kafka with django
1)cd to the galificdatapipeline directory and type the command "python manage.py shell".
2)In the shell opened, run the python file "kafka-consumer.py" located at galificdatapipeline/websocket/kafka-consumer.py

Step 4:Running the whole pipeline
1)Run the python file "mimic-server" and open the link "localhost/abc/"

Control Flow :->
1)mimic-server.py :-> creates data and push it into kafka server.
2)Kafka server :-> acts as the data pipeline to transfer data in realtime.
3)kafka-consumer.py :->Receives the data from pipeline,Cleans the data.
    (i)Connect to a Mongodb database and updates the database and return the new updated object/row.
    (ii)Sends the new updated object/row to the socket.
4)Socket:-> (i)The received data  first reaches user_galific fxn in GalificConsumer class in consumer.py.
    (ii)The data is then send to the url present at routing.py
5)Webpage:->The data from websocket is recieved and then shown using javascript.

