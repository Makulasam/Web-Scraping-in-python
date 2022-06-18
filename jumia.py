import requests as rs
from bs4 import BeautifulSoup as bs
import csv

jumia_page = rs.get('https://www.jumia.ug/catalog/?q=beers')

# turn page into a BeautifulSoup object
soup=bs(jumia_page.content,'lxml')

#getting the names of all the brands
names=[]
for name in soup.find_all(class_='name'):
    names.append(name.string)
    

#getting the prices of brands
prices=[]
for price in soup.find_all(class_='prc'):
    prices.append(price.string)
    

#get the old price the brand
old_prices=[]
for old_price in soup.find_all(class_='old'):
    old_prices.append(old_price.string)
   
#getting percenatage of discount
discounts=[]
for discount in soup.find_all(class_='tag _dsct _sm'):
    discounts.append(discount.string)
    


""" writing data to CSV """

# open top25.csv file in "write" mode
with open('Alcohol_on_jumia.csv', 'w') as file:
  # create a "writer" object
  writer = csv.writer(file, delimiter=',')

  # use "writer" obj to write 
  # you should give a "list"
  writer.writerow(["Name", "New Price", "Old Price", "Discounts"])

  for i in range(25):
    writer.writerow([
      names[i],
        prices[i],
        old_prices[i],
        discounts[i],
    ])