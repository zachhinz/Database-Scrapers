from selenium import webdriver

from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib

#Data Sheet
df = pd.read_excel("CDO Dataset, Sheet 3 Modified.xlsx", header = 0)

#Sign in Process with Duo :(
driver = start_chrome('https://pomona.joinhandshake.com/login')
click('Sign In')
write('zcha2020@mymail.pomona.edu')
click(Button('Next'))
click('Pomona College Sign On')
write('zcha2020@mymail.pomona.edu')

next_box = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
next_box.click()

write('password', into='Password')
click('sign in')
click('Yes, trust browser')
click(Button('Yes'))
click(Link('Manage'))

#List of IDs
IDList = set(df['ID'].tolist())

start = 0
IDList = IDList[start:]

for id in IDList:
    #Go to Correct Tab given id
    click(Link('Manage'))
    click(S('#query'))
    print(IDList.index(id)+start)
    print(id)
    write(id)
    click(S("#search_button"))

    #Naviagte to the correct page
    click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr[1]/td[2]/a'))
    click(Link('Account'))
    Config.implicit_wait_secs = 100

    click(S('//*[@id="nav-pills-container"]/li[1]/a'))
    Config.implicit_wait_secs = 100
        
    #Scrap HTML
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

    workExperiences = soup.find('div', {'class': 'style__card___1rhof'})
    for ex in workExperiences:
        print(ex.get_text())
    '''

    jobElements = soup.find_all("div", {'class': "style__flex___fCvpa style__justify-space-between___F3m5J"})
    job = df.loc[IDList.index(id)+start, 'Work Experiences Position']
    print(job)

    for jobElement in jobElements:
        if(jobElement != None):
            jobText = jobElement.find('h3', {'class':'style__heading___29i1Z style__medium___m_Ip7'}).get_text()
            print(jobText)

            nextElement = jobElement.find_next_sibling()
            if(nextElement!=None and jobText==job):
                dateElement = nextElement.find('span')
                print(dateElement.get_text().split(' - ')[0])
                break'''