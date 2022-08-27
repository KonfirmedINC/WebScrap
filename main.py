from bs4 import BeautifulSoup
import requests

url = ("https://blackbusinessdirect.ca/listings/british-columbia/")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
job = soup.find('div', class_='container-fluid item-list')
job_elements = job.find_all("div", class_="row list-item mb-4 mx-3 mx-sm-0")
for job_element in job_elements:
    name = job_element.find("h4", class_="mb-2").text.replace('\t', '').replace('\n','')
    description = job_element.find("div", class_="card-text mb-2").text.replace('\t', '').replace('\n','')
    location = job_element.find("div", class_="address flex-grow-1").text.replace('\t', '').replace('\n','').replace('BC', 'BC ').replace('604-', ' 604-').replace('(604', ' (604').replace('1-778', ' 1-778').replace('778', ' 778')
    
    website = job_element.find("a", class_="text-green").get('href')
    header = ['Name','Description','Address','Url']
    telephone = soup.find("div", {"class": "tel"}).a.__getitem__('href')
    info = [name, description, location, telephone, website]

    print('')
    print(name)
    print(description)
    print(location)
    print(telephone)
    print('')

    # print(website)
