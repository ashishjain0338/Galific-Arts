from kafka import KafkaProducer
import random
import time
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
Emailid = ['test1@gmail.com','test2@gmail.com','test3@gmail.com','test4@gmail.com']
category = ['watches','frames','Tshirts','Jeans']
for x in range(0,12):
    i = random.randint(0,3)
    j = random.randint(0,3)
    str = Emailid[i] + ','+category[j]
    producer.send('GalificData', bytes(str, 'utf-8') )

    print(str)
    time.sleep(1)

