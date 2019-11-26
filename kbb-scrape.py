import urllib.request
from bs4 import BeautifulSoup as bs
import csv

with open('kbb-output.csv', 'w') as f:
  writer = csv.writer(f)

  headers = ['mileage', 'body', 'extcol', 'intcol', 'fuecon',
             'engine', 'ftype', 'trans', 'dtype', 'doors',
             'make_model']

  writer.writerow(headers)

  # loop through each page
  for pg in range(1, 41):
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

      # get car details from KBB
      car_details_list_scraped = [detail.text.strip() for detail in soup_2.find('div', class_='details-list').find_all('li')]

      # allocate everything to a dict, while accounting for missing details
      # headers_complete contain headers that are the same as those on KBB, letter for letter
      # this is for matching purposes in the for loop down below
      headers_complete = ['Mileage', 'Body Style', 'Exterior Color', 'Interior Color', 'Fuel Economy',
                          'Engine', 'Fuel Type', 'Transmission', 'Drive Type', 'Doors']

      car_details_list_organized = dict.fromkeys(headers_complete, '')

      # loop thru all the keys in headers_complete
      for index in range(len(headers_complete)):
        for detail in car_details_list_scraped:
          key = headers_complete[index]

          # go thru and check if the header exists on the site,
          # if it's there, add it to the dict
          if detail.split(': ')[0] == key:
            car_details_list_organized[key] = detail.split(': ')[1]

      # finally, insert make_model to car_details_list_organized
      car_details_list_organized['Make_Model'] = make_model

      # write it out to csv file
      writer.writerow(car_details_list_organized.values())

    print('done with page', pg)
