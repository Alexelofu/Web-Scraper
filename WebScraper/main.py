from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


html_text = requests.get('https://www.indeed.co.uk/jobs?q=Data+Scientist&l=Scotland&from=sug').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')



for job in jobs:
    company_name = job.find("span", class_ ="company").text.replace(' ', '')
    job_title = job.h2.a['title']
    more_info = job.h2.a['href']
    skills = job.find('div', class_ = "summary").text
    published_date =  job.find('span', class_ = "date").text

    print(f"Company Name: {company_name.strip()} \n")
    print(f"Job Title: {job_title} \n")
    print(f"Require Skills: {skills.strip()} \n")
    print(f"More Info: https://www.indeed.co.uk{more_info}")
    print(f"Published Date: {published_date} \n \n \n")
   
