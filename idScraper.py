from helium import *
from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib

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

#Not my real password of course
write('Password', into='Password')
click('sign in')
click('Yes, trust browser')
click(Button('Yes'))
click(Link('Manage'))

#Helpful for trackin progress
start = 0

#List of Names, First and Last
nameListTest = nameTestdf['Name'].tolist()
nameList = nameListdf['Name'].tolist()
nameList = nameList[start:85]

for name in nameList:
    #Go to Correct Tab given name
    click(S('#query'))
    print(name)
    print(nameList.index(name)+start)
    write(name)
    click(S("#search_button"))
    Config().implicit_wait_secs = 100
    click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr[1]/td[1]'))

    #A search might bring 0, 1, 2 or more entries with that particular name
    page = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(page, "html.parser")  
    numRows = len(soup.find_all('a', string = (name.split())[1]))
    print(soup.find_all('a', string = (name.split())[1]))
    print(numRows)    

    idNumber = 1

    if(numRows==0): # Check Again
        click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr/td[2]/a'))
        click(Link('Account'))   
        idNumber = 0
    
    if(numRows<=1): #One record found
        click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr/td[2]/a'))
        click(Link('Account'))
        click(S('//*[@id="user_username"]'))

        #Scrap HTML
        page = driver.execute_script("return document.body.innerHTML;")
        soup = BeautifulSoup(page, "html.parser")

        #Find idNumber
        idNumber = soup.find(id="user_username").get('value')

    elif(numRows>1): #Entry must be checked further, multiple people with the same name
        click(S('//*[@id="search-form"]/div/div/div/div[4]/div/div[2]/div[1]/div/div[9]/table/tbody/tr/td[2]/a'))
        click(Link('Account'))   
        idNumber = 2  

    print(idNumber)

    #Input ID for each name in the list
    instances = (nameListdf.index[nameListdf['Name'] == name].tolist())
    nameListdf.loc[instances[0], 'ID'] = int(idNumber)
    nameListdf.to_excel('NameList.xlsx', index = False)

    click(Link('Manage'))