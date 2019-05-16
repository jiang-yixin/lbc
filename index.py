import urllib.request
import json

# get all posts
lbcFileName = "20190516-77-LT-100K"
f = urllib.request.urlopen('https://raw.githubusercontent.com/jiang-yixin/lbc/master/input/' + lbcFileName + '.json')
posts = json.loads(f.read())

# get populations 
# ex. {'nom': 'Wy-dit-Joli-Village', 'code': '95690', 'codeDepartement': '95', 'codeRegion': '11', 'codesPostaux': ['95420'], 'population': 335}
f = urllib.request.urlopen('https://raw.githubusercontent.com/jiang-yixin/lbc/master/input/population-ile-de-france.json')
cities = json.loads(f.read())

#for i in range(len(cities)):
    #print(cities[i])


file = open("./output/" + lbcFileName + ".csv","w")
 
file.write("title,url,price,city,zipCode,population\n")

for i in range(len(posts)):
    zipCode = posts[i]['zipCode']
    city = posts[i]['city']
    population = 0
    for j in range(len(cities)):
        if zipCode in cities[j]['codesPostaux']:
            population = cities[j]['population']
    text = posts[i]['title'] + ',' + posts[i]['url'] + ',' + posts[i]['price'] + ',' + city + ',' + zipCode + ',' + str(population)

    print (text)
    file.write(text + '\n')

file.close() 

#for i in range(len(posts)):
#    print(posts[i])


#print (posts)