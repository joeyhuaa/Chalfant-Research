import urllib.request
from bs4 import BeautifulSoup as bs
import csv
from multiprocessing import Pool


def parse(url):
  sauce_2 = urllib.request.urlopen(url).read()
  soup_2 = bs(sauce_2, 'html.parser')

  # get car details from KBB
  car_details_list_scraped = [detail.text.strip() for detail in soup_2.find('div', class_='details-list').find_all('li')]

  # allocate everything to a dict, while accounting for missing details
  # headers_complete contain headers that are the same as those on KBB, letter for letter
  # this is for matching purposes in the for loop down below
  headers_complete = ['Mileage', 'Body Style', 'Exterior Color', 'Interior Color', 'Fuel Economy',
                      'Engine', 'Fuel Type', 'Transmission', 'Drive Type', 'Doors']

  car_details_dict_organized = dict.fromkeys(headers_complete, '')

  # loop thru all the keys in headers_complete
  for index in range(len(headers_complete)):
    for detail in car_details_list_scraped:
      key = headers_complete[index]

      # go thru and check if the header exists on the site,
      # if it's there, add it to the dict
      if detail.split(': ')[0] == key:
        car_details_dict_organized[key] = detail.split(': ')[1]

  # finally, insert car_title and price to car_details_list_organized
  car_title = soup_2.find('h1', class_='primary-vehicle-title').text.strip()
  price = soup_2.find('span', class_='js-price').text.strip().replace('$', '').replace(',', '')

  car_details_list_organized = list(car_details_dict_organized.values())

  car_details_list_organized.insert(0, car_title)
  car_details_list_organized.insert(1, price)

  # append is too slow! return instead
  return car_details_list_organized

# write to csv
with open('kbb-output.csv', 'w') as f:
  writer = csv.writer(f)

  headers = ['car_title', 'price', 'mileage', 'body', 'extcol', 'intcol',
             'fuecon', 'engine', 'ftype', 'trans', 'dtype',
             'doors']

  # write headers
  writer.writerow(headers)

  # loop through each page
  for pg in range(1, 41):

    # to capture each round of scraping
    records = []

    url = 'https://www.kbb.com/cars-for-sale/cars/?p=' + str(pg) + '&distance=75&searchtype=used&atcmodelcode=all&nr=25&atcmakecode=honda&atctrim=all'
    sauce = urllib.request.urlopen(url).read()
    soup = bs(sauce, 'html.parser')

    print('on page', pg)

    # compile all the listing links
    listing_hrefs = [a['href'] for a in soup.find_all('a', class_='js-vehicle-name')]
    listing_urls = ['https://www.kbb.com' + str(href) for href in listing_hrefs]

    # pool each page with 28 parallel processes and write to csv
    pool = Pool(28)
    records.append(pool.map(parse, listing_urls))
    pool.terminate()
    pool.join()

    # write record to csv
    for record in records:
      for rec in record:
        writer.writerow(rec)
        print(rec)

    print('done with page', pg)




