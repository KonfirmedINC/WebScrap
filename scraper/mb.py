from bs4 import BeautifulSoup
import requests

url = ("https://blackbusinessdirect.ca/listings/manitoba")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
job = soup.find('div', class_='container-fluid item-list')
job_elements = job.find_all("div", class_="row list-item mb-4 mx-3 mx-sm-0")
for job_element in job_elements:
    name = job_element.find("h4", class_="mb-2").text.replace('\t', '').replace('\n','')
    description = job_element.find("div", class_="card-text mb-2").text.replace('\t', '').replace('\n','')
    location = job_element.find("div", class_="address flex-grow-1").text.replace('\t', '').replace('\n','').replace('MBR', 'MB R').replace('4N5431', '4N5 431').replace('866', ' 866').replace('MBR0M', 'MB R0M').replace('204', ' 204').replace('1888', ' 1 888').replace('709', ' 709').replace('2R31 ', ' 2R3 1').replace('800-', ' 800-').replace('1X01  ', '1X0 1 ').replace('1204', '1 204')
    industry = job_element.find("span", class_="cat-name-figure rounded p-2").text.replace('&amp;', '&')
    telephone = job_element.find("div", class_="tel").find("a", class_="").get_text('').replace('\t', '').replace('\n','')
    # website = job_element.find("a", class_="text-green").get('href')

    info = [name, description, location, telephone, industry]

    print('*------------*')
    print('Company name:', name)
    print('Description:', description)
    print('Location:', location)
    print('Industry:', industry)
    # print('Telephone:', telephone)
    print('*------------*')