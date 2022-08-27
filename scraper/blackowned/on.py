from bs4 import BeautifulSoup
import requests

url = ("https://blackownedcanada.org/listing-category/ontario/")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
prejob = soup.find('div', class_='bpro-listing-grid ') 
job = soup.find_all('div', class_='bpro-listing-grid-content-outer')
job_elements = soup.find_all("div", class_="bpro-listing-grid-content")
for job_element in job_elements:
    name = job_element.find("h3", class_="").text
    # name = job_element.find("h3", class_="").text.replace('\t', '').replace('\n','')
    # description = job_element.find("div", class_="card-text mb-2").text.replace('\t', '').replace('\n','')
    # location = job_element.find("div", class_="address flex-grow-1").text.replace('\t', '').replace('\n','').replace('AB', 'AB ').replace('403-', ' 403-').replace('780', ' 780').replace('(403)', ' (403)').replace('844', ' 844').replace('6V1J6?', '6V1J6')
    # industry = job_element.find("span", class_="cat-name-figure rounded p-2").text.replace('&amp;', '&')
    # telephone = soup.find("div", {"class": "tel"}).a.__getitem__('href')
    # website = job_element.find("a", class_="text-green").get('href')


    print('*------------*')
    print('Company name:', name)
    # print('Description:', description)
    # print('Location:', location)
    # print('Industry:', industry)
    # print('Telephone:', telephone)
    print('*------------*')