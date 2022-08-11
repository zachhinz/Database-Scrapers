from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib

#Data Sheet
nameTestdf = pd.read_excel("NamesTest.xlsx", header = 0)
nameListdf = pd.read_excel("NameList.xlsx", header = 0)

#Sign in Process with Duo :(
driver = start_chrome('https://pomona.joinhandshake.com/login')
click('Sign In')
write('zcha2020@mymail.pomona.edu')
click(Button('Next'))
click('Pomona College Sign On')
write('zcha2020@mymail.pomona.edu')
next_box = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
next_box.click()
write('Password', into='Password')
click('sign in')
click('Yes, trust browser')
click(Button('Yes'))
click(Link('Manage'))

#List of IDs
testIDList = nameTestdf['ID'].tolist()
IDList = nameListdf['ID'].tolist()

start = 351
IDList = IDList[start:]

for id in IDList:
   #Go to Correct Tab given id
    click(Link('Manage'))
    click(S('#query'))
    print(IDList.index(id)+start)
    print(id)
    write(id)
    click(S("#search_button"))
    click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr[1]/td[2]/a'))
    click(Link('Account'))
    Config.implicit_wait_secs = 100
    click(S('//*[@id="nav-pills-container"]/li[1]/a'))
    Config.implicit_wait_secs = 100
        
    #Scrap HTML
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

   
    #Find major
    major  = 'None'
    foundName = soup.find('h1')
    majorList = soup.find_all("h3", {"class": "style__heading___29i1Z style__medium___m_Ip7 style__fitted___3L0Tr"})
    
    #Make sure the system actually reads the HTML, and doesn't click this particular entry
    if(len(majorList)!=0 and foundName != 'A. Szafran'):
      major = majorList[1].get_text()
    print(major)
    
    #Input ID for each name in the list
    instances = (nameListdf.index[nameListdf['ID'] == id].tolist())
    nameListdf.loc[instances[0], 'Major'] = major
    nameListdf.to_excel('NameList.xlsx', index = False)

    click(Link('Manage'))