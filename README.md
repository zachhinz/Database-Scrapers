# Database-Scrapers

As part of my work as a Data Analytics Intern at Pomona's CDO in the 
Summer of 2022, I was asked to gather several attributes of data for a 
large excel spreadsheet of recent students who participated in 
internships or on campus jobs. This excel sheet had some 3,500+ entries,
 and so finding the attributes (ID number, major(s), Visa status) for 
each entry would be extremely tedious. To automate the process, I 
created a series of python webscrapers used to scrap data from a large 
internal Handshake database. Using Helium (a superset of Selenium Chrome
 driver) I could navigate to the proper web page, grab the HTML, parse 
it, and put it into the correct Excel column. Interacting with excel was
 done through the Pandas library. In my experience, using Helium has 
been successful if a bit glitchy. It will throw a Stale Frame Exception 
roughly every few hundred repeats of the main for loop randomnly, and 
sometimes it will throw an element not interactable exception for a 
button. But ultimately this combination of Pandas and Helium got the job
 done.
