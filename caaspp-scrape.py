import urllib.request
import requests
import json
from bs4 import BeautifulSoup as bs
import csv

# fetch headers from website
url_web = 'http://caaspp.edsource.org/'
sauce_2 = urllib.request.urlopen(url_web)
soup = bs(sauce_2, 'html.parser')
headers = [th.text.strip() for th in soup.find('tr').find_all('th')]

# fetch actual data
url_json = 'http://caaspp.edsource.org/allschools.json?_=1576355511547'
sauce = requests.get(url_json)
json = json.loads(sauce.text)['data']
all_data = []       # data will be stored in lists within a list

for i in range(len(json)):
  data = []
  for j in range(len(json[i])):
    if j == 0:
      district = json[i][0].split('>')[1].split('<')[0]
      data.append(district)
    else:
      data.append(json[i][j])
  all_data.append(data)

with open('caaspp-output.csv', 'w') as f:
  w = csv.writer(f)
  w.writerow(headers)
  for data in all_data:
    w.writerow(data)







