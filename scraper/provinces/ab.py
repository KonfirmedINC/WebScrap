from bs4 import BeautifulSoup
import requests

url = ("https://blackbusinessdirect.ca/listings/alberta")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
job = soup.find('div', class_='container-fluid item-list')
job_elements = job.find_all("div", class_="row list-item mb-4 mx-3 mx-sm-0")
for job_element in job_elements:
    name = job_element.find("h4", class_="mb-2").text.replace('\t', '').replace('\n','')
    description = job_element.find("div", class_="card-text mb-2").text.replace('\t', '').replace('\n','')
    location = job_element.find("div", class_="address flex-grow-1").text.replace('\t', '').replace('\n','').replace('AB', 'AB ').replace('403-', ' 403-').replace('780', ' 780').replace('(403)', ' (403)').replace('844', ' 844').replace('6V1J6?', '6V1J6')
    industry = job_element.find("span", class_="cat-name-figure rounded p-2").text.replace('&amp;', '&')
    telephone = soup.find("div", {"class": "tel"}).a.__getitem__('href')
    # website = job_element.find("a", class_="text-green").get('href')

    info = [name, description, location, telephone, industry]

    print('*------------*')
    print('Company name:', name)
    print('Description:', description)
    print('Location:', location)
    print('Industry:', industry)
    print('Telephone:', telephone)
    print('*------------*')