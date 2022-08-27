from contextlib import nullcontext
from types import NoneType
from bs4 import BeautifulSoup
import requests

url = ("https://blackbusinessdirect.ca/listings/quebec")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
job = soup.find('div', class_='container-fluid item-list')
job_elements = job.find_all("div", class_="row list-item mb-4 mx-3 mx-sm-0")
for job_element in job_elements:
    name = job_element.find("h4", class_="mb-2").text.replace('\t', '').replace('\n','')
    description = job_element.find("div", class_="card-text mb-2").text.replace('\t', '').replace('\n','')
    location = job_element.find("div", class_="address flex-grow-1").text.replace('\t', '').replace('\n','').replace('902-3147747', '').replace('PEI - ', '').replace('PE', 'PEI').replace('charlottetown, C', 'C')
    telephone = job_element.find("div", class_="tel").text.replace('\t', '').replace('\n','')
    # telephone = soup.find("div", {"class": "tel"}).a.__getitem__('href')
    industry = job_element.find("span", class_="cat-name-figure rounded p-2").text
    header = ['Name', 'Description', 'Address', 'Telephone', 'Industry']

    info = [name, description, location, telephone, industry]

    print('*------------*')
    print('Company name:', name)
    print('Description:', description)
    print('Location:', location)
    print('Industry:', industry)
    print('Telephone:', telephone)
    print('*------------*')
