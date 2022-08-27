from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

url = ("https://blackbusinessdirect.ca/listings/british-columbia/vancouver-2")
page = requests.get(url)
# html_text = requests.get('https://blackbusinessdirect.ca/listings/british-columbia/vancouver-2').text
# print(html_text)
soup = BeautifulSoup(page.content, 'html.parser')
job = soup.find('div', class_='container-fluid item-list')
job_elements = job.find_all("div", class_="row list-item mb-4 mx-3 mx-sm-0")
for job_element in job_elements:
    name = job_element.find("h4", class_="mb-2").text.replace('\t', '').replace('\n','')
    description = job_element.find("div", class_="card-text mb-2").text.replace('\t', '').replace('\n','')
    location = job_element.find("div", class_="address flex-grow-1").text.replace('\t', '').replace('\n','').replace('BC', 'BC ').replace('604-', ' 604-').replace('(604', ' (604').replace('1-778', ' 1-778').replace('778', ' 778')
    # telephone = job_element.find("div", class_="tel").text.get('href')
    website = job_element.find("a", class_="text-green").get('href')
    header = ['Name','Description','Address','Url']
    info = [name, description, location, website]
    # with open('blackbusinessesincanada.csv', 'w', encoding='utf8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     writer.writerows(info)

    print(name)
    print(description)
    print(location)
    # print(telephone)
    print(website)
    print()
