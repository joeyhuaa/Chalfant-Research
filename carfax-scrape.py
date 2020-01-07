import csv
import json
import requests

with open('carfax-output.csv', 'w') as f:
  writer = csv.writer(f)
  headings = ['make', 'model', 'price', 'year',
              'mileage', 'engine', 'extCol', 'intCol', 'trans',
              'dtype', 'mpgCity', 'mpgHw', 'condition']
  writer.writerow(headings)

  for pg in range(1, 51):
    url = 'https://www.carfax.com/api/vehicles?zip=95616&radius=50&sort=BEST&dynamicRadius=false&make=Honda&page=' + str(pg)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    headers = {'User-Agent': user_agent}

    sauce = requests.get(url, headers=headers)
    json = json.loads(sauce.text)

    for listing in json['listings']:
      car_info = []
      car_info.append(listing['make'])
      car_info.append(listing['model'])
      car_info.append(listing['listPrice'])
      car_info.append(listing['year'])
      car_info.append(listing['mileage'])
      car_info.append(listing['engine'])
      car_info.append(listing['exteriorColor'])
      car_info.append(listing['interiorColor'])
      car_info.append(listing['transmission'])
      car_info.append(listing['drivetype'])
      car_info.append(listing['mpgCity'])
      car_info.append(listing['mpgHighway'])
      car_info.append(listing['vehicleCondition'])
      writer.writerow(car_info)
    print('done with page', str(pg))



















