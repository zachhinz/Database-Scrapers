from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib

#Used to check all IDs against names, just to ensure that everything is absolutely correct
#ID numbers were used for further attributes, as they always brought up exactly one data entry

#Data Sheets, test and real
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

write('Password!', into='Password')
click('sign in')
click('Yes, trust browser')
click(Button('Yes'))
click(Link('Manage'))

#List of IDs
testIDList = nameTestdf['ID'].tolist()
IDList = nameListdf['ID'].tolist()

#Done in several stages
start = 1388
IDList = IDList[start:]

for id in IDList:
    #Go to Correct Tab given ID
    click(Link('Manage'))

    click(S('#query'))
    print(IDList.index(id)+start)
    print(id)
    write(id)
    click(S("#search_button"))
    Config().implicit_wait_secs = 100
    click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr/td[2]/a'))
    click(Link('Account'))
        
    #Scrap HTML
    page = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(page, "html.parser")

    #Find Name attached to ID
    foundName = (soup.find("span", {"class": "student-profile-card__details-label"}))
    print(foundName)

    #Check if attached Name is same as what we've got
    idIndex = (nameListdf.index[nameListdf['ID']==id].tolist())[0]
    givenName = nameListdf.loc[idIndex,'Name']

    if(givenName!=foundName):
        nameListdf.loc[idIndex, 'Checker'] = 1
        nameListdf.to_excel('NameList.xlsx', index = False)
    elif(givenName==foundName):
        nameListdf.loc[idIndex, 'Checker'] = 0
        nameListdf.to_excel('NameList.xlsx', index = False)

    click(Link('Manage'))