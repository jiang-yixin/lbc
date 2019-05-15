import urllib.request
import json

f = urllib.request.urlopen('https://raw.githubusercontent.com/jiang-yixin/lbc/master/test.json')
jsonData = json.loads(f.read())
print (jsonData)