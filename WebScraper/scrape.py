from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'}
    url = f'https://www.indeed.com/jobs?q=data+scientist+$20,000&l=New+York&start={page}'
    r = requests.get(url, headers)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    jobs = soup.find_all('div', class_ = "jobsearch-SerpJobCard")
    #return len(jobs)
    for item in jobs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = 'None'
        
        summary = item.find('div', {"class" : 'summary'}).text.strip().replace('\n','' )

        #Creating a dictionary for all the scraped items
        job = {
            'Title' : title,
            'Company': company,
            'Salary': salary,
            'Summary': summary
        }
        #Appending all the scraped items and forming a list according to our dictionary
        joblist.append(job)
    
    return

#Creating an empty list called joblist
joblist = []

 


#Iterating through the pages as the pages change in 10's so we move from 0 - 30 giving 3 pages
for i in range(0, 40, 10):
    print(f'Getting page, {i}') #tells us what page we are on
    #extract page 1 and prints the number of divs that match the class on the first page
    c = extract(i)

    #print(transform(c))
    transform(c)
    
#Creating a dataframe 
df = pd.DataFrame(joblist)
print(df.head(40))

#Converting to CSV
df.to_csv('jobs.csv')
