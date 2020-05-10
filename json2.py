import json
import urllib.request, urllib.error, urllib.parse


data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_521587.json')
data1 = data.read()

info = json.loads(data1)
print('User count:', len(info))
sum = 0

for x in info['comments']:

    sum += int(x['count'])
print(sum)
