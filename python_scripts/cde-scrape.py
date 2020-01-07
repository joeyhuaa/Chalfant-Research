import urllib.request
from bs4 import BeautifulSoup as bs
import csv

years = ['2017-18', '2016-17', '2015-16', '2014-15', '2013-14']

for y in years:
  url = 'https://data1.cde.ca.gov/dataquest/satactap/CollegeTest?cdscode=00000000000000&CollegeTest=sat&year=' + y

  sauce = urllib.request.urlopen(url).read()
  soup = bs(sauce, 'html.parser')

  # fetch all table row elements
  trs = soup.find_all('tr')

  # the first table row has all the headers
  headers = [th.text.strip() for th in trs[0].find_all('th')]

  with open('cde-output' + y + '.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(headers)

    # fetch rest of data
    for tr in trs[1:]:
      row_data = [td.text.strip() for td in tr.find_all('td')]
      w.writerow(row_data)









