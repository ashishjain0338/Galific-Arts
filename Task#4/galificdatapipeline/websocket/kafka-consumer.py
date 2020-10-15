from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from kafka import KafkaConsumer
from pymongo import MongoClient
import datetime

def sendtosocket(email,category,visits,lastvisit):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "realtimedata",{
            "type" : "user.galific",
            "EmailId"  : email,
            "category" : category,
            "visits" : visits,
            "lastvisit": lastvisit
        }
    )

def storetoMongodb(email , category):
    var1 = MongoClient()
    db = var1.GalificArts
    Coll = db.Visits
    data = Coll.find_one({'EmailId': email})
    if (data == None):
        #If user doesn't exist
        data = {'EmailId': email, 'category': [category], 'visits': [1],
                'lastvisit': [datetime.datetime.now()]}
        Coll.insert_one(data)
    else:
        #if the user has visited that category multiple times
        if category in data['category']:
            ind = data['category'].index(category)
            data['visits'][ind] += 1
            data['lastvisit'][ind] = datetime.datetime.now()
            Coll.update_one({'EmailId': email}, {'$set': data})
        else:
            data['category'].append(category)
            data['visits'].append(1)
            data['lastvisit'].append(datetime.datetime.now())
            Coll.update_one({'EmailId': email}, {'$set': data})
    return Coll.find_one({'EmailId': email})

#Establishing the connection to kafka for realtime data processing
consumer = KafkaConsumer('GalificData',bootstrap_servers='localhost:9092')
for data in consumer:
    x = data.value
    x = x.decode("utf-8") #converting bytes to string
    clean_data = x.split(',')
    email = clean_data[0]
    category = clean_data[1]
    #Storing the data to mongodb database and retrieving the updated object
    mongodbdata = storetoMongodb(email , category)
    print(mongodbdata)
    #Sending the updated data to our socket
    date_time = [x.strftime("%m/%d/%Y, %H:%M:%S") for x in mongodbdata['lastvisit']]
    sendtosocket(mongodbdata["EmailId"],mongodbdata["category"],mongodbdata["visits"],date_time)
