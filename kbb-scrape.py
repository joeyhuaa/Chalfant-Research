import urllib.request
from bs4 import BeautifulSoup as bs
import csv

with open('kbb-output.csv', 'w') as f:
  writer = csv.writer(f)

  headers = ['mileage', 'body', 'extcol', 'intcol', 'fuecon',
             'engine', 'fuetype', 'trans', 'drivetype', 'doors',
             'make_model']

  writer.writerow(headers)

  # price
  # model and make

  for pg in range(1,41):
    url = 'https://www.kbb.com/cars-for-sale/cars/?p=' + str(pg) + '&distance=75&searchtype=used&atcmodelcode=all&nr=25&atcmakecode=honda&atctrim=all'
    sauce = urllib.request.urlopen(url).read()
    soup = bs(sauce, 'html.parser')

    print('on page', pg)

    # find all listings
    for listing in soup.find_all('div', class_='listing'):

      # locate href
      href = listing.find('a', class_='js-vehicle-name')['href']
      make_model = listing.find('a', class_='js-vehicle-name').text.strip()

      # navigate to href
      url_2 = 'https://www.kbb.com' + href
      sauce_2 = urllib.request.urlopen(url_2).read()
      soup_2 = bs(sauce_2, 'html.parser')

      # get car details
      # fuck yeah!! list comprehension!!
      car_details = soup_2.find('div', class_='details-list').find_all('li')
      car_details_list = [detail.text.split(': ')[1].strip() for detail in car_details if detail.text.split(': ')[1].strip() != '']

      # get make and model
      car_details_list.append(make_model)

      # write everything to csv
      writer.writerow(car_details_list)

    print('done with page', pg)