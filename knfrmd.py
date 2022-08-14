from bs4 import BeautifulSoup
import requests
from csv import writer

url = ("https://blackownedcanada.org/listing-category/ontario/")
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="bpro-listing-grid")

with open('blackbusinessesincanada.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Call', 'Map', 'Location']
    thewriter.writerow(header)
for list in lists:
    title = list.find('div', class_="bpro-listing-grid-content")
    call = list.find('a', class_="grind-number")
    map = list.find('li',class_="show-loop-map-popup")
    location = list.find('p', class_="bpro-grid-city")
    info = [title, call, map, location]
    thewriter.writerow(info)

# for list in lists:
#     title = list.find('div', class_="bpro-listing-grid-content").text.replace(' ', '')
#     call = list.find('a', class_="grind-number").text.replace(' ', '')
#     map = list.find('li',class_="show-loop-map-popup").text.replace(' ', '')
#     info = [title, call, map]
#     print(info)



# job = soup.find('li', class_ ='b_algo')
# job.find 





# url="https://www.bing.com/"
# page = requests.get(url)


# soup = BeautifulSoup(page.content, 'html.parser')
# lists = soup.find_all('section',class_="listing-search-item")

