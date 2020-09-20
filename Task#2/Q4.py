import simplejson as Json
import requests
#Getting weather data of longitude = 113.17 and lattitude = 23.098
response = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=civil&output=json")
print(response.status_code)
#Opening Two files Json and Txt file to store data named under webapi
file = open('webapi.json','w')
file2 = open('webapi.txt','w')
data = response.json()
dict1 = {}
header = ""
for x in data['dataseries']:
    for y in x.keys():
        if type(x[y]) == type(dict1):
            for z in x[y].keys():
                header = header + str(z) + '\t'
        else:
            header = header + str(y) + '\t'
    break
header+='\n'
file2.write(header)

for x in data['dataseries']:
    writing_str = ""
    for y in x.values():
        if type(y) == type(dict1):
            for z in y.values():
                writing_str = writing_str + str(z) + '\t\t\t'
        else:
            writing_str = writing_str + str(y) + '\t\t\t'
    writing_str+='\n'
    #Writing the data to txt file
    file2.write(writing_str)

#Writing the data to json file
Json.dump( data , file ,indent = 4)