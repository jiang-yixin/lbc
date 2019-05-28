import urllib.request
import json

# get all posts
lbcFileName = "coloc/20190528-TEST"
f = urllib.request.urlopen('https://raw.githubusercontent.com/jiang-yixin/lbc/master/input/' + lbcFileName + '.json')
posts = json.loads(f.read())

# get the list of cities
cities = {}
for i in range(len(posts)):
    cityName = posts[i]['name']
    if cityName not in cities:
        cities[cityName] = 1
    else:
        cities[cityName] += 1

citiesSorted = sorted(cities.items(), key=lambda x: x[1], reverse=True)

file = open("./output/" + lbcFileName + ".csv","w")
file.write("number,city\n")

for key, value in citiesSorted:
    text = str(value) + ',' +  str(key)
    print (text)
    file.write(text + '\n')
    
file.close()