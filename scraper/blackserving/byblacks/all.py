from types import NoneType
from typing import Text
from bs4 import BeautifulSoup
import requests

url = ("https://byblacks.com/directory/black-youth-family-services/page")
for page in range(1,3):
    response = requests.get(url + str(page) + '/')
    soup = BeautifulSoup(response.text, 'html.parser')
    job_elements = soup.find_all("div", class_="lsrow row-fluid")
    count = 0
    for job_element in job_elements:
        name = job_element.find("div", class_="mt-ls-header").text.replace('\t', '').replace('\n','')
        try:
            location = job_element.find("div", class_="mt-ls-fields address").text.replace('\t', '').replace('\n','')
        except AttributeError:
            location = job_element.find("div", class_="mt-ls-fields address")
        try: category = job_element.find("span", class_="output").text.replace('\t', '').replace('\n','')
        except AttributeError:
            category = job_element.find("span", class_="output")
        telephone = soup.find("div", {"class": "mt-ls-field mfieldtype_coretelephone span12 lastFieldRow"}).find("span", class_="output").text
        count += 1

        print(count)
        print('*------------*')
        print('Company name:', name)
        print('Location:', location)
        print('Category:', category)
        print('Telephone:', telephone)
        print('*------------*')
