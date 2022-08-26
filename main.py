from bs4 import BeautifulSoup
import requests
from csv import writer

url = ("https://blackbusinessdirect.ca/listings/british-columbia/vancouver-2")
page = requests.get(url)
# html_text = requests.get('https://blackbusinessdirect.ca/listings/british-columbia/vancouver-2').text
# print(html_text)
soup = BeautifulSoup(page.content, 'html.parser')
job = soup.find('div', class_='container-fluid item-list')
container = soup.find_all('div', class_='row list-item mb-4 mx-3 mx-sm-0')[0]
list_items = container.find_all('div', 'col-sm-7 px-sm-3 py-3 pt-sm-0 pl-sm-4')
with open('blackbusinessesincanada.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Company', 'Address', 'Tel', 'Url']
    thewriter.writerow(header)
for list_item in list_items:

    company_name = list_item.find('div', class_='flex-grow-1')
    # location = job.find('div', class_='address flex-grow-1')
    location = list_item.find('div', class_='address flex-grow-1')
    contact = list_item.find('div', class_='tel')
    website = list_item.find('h4', class_='mb-2')
info = [company_name.text.replace('\t',''), location.text.replace('\t',''), contact.text.replace('\t',''), website.a.get('href')]
thewriter.writerow(info)
# print(info)
#     title = list.find('div', class_='')
# print('''
# Company Name: {company_name}
# Address: {location}
# Tel: {contact}
# Url: {website}
# ''')
# print(company_name.text)
# print(location.text)
# print(contact.text)
# print(website.a.get('href'))
# url="https://blackbusinessdirect.ca/listings/british-columbia/vancouver-2"
# page = requests.get(url)
# print(page)
# soup = BeautifulSoup(page.content, 'html.parser')
# lists = soup.find_all('div', class_="listText")
# for list in lists:
#     title = list.find('span', class_="itemName").text
    # location = list.find('span', class_="buttonText")
    # website = list.find('a', 'href', class_="biglink clearfix")
    # info = [title]
    # print(info)