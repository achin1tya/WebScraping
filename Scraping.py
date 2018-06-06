import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('http://www.iato.in/members/lists')			# getting the iato webpage into beautiful soup 

soup = BeautifulSoup(page.text, 'html.parser')					# getting html elements from page
 
last_links = soup.find(class_="post-content")					# generating required links 
last_links_item=last_links.find_all('a');



links=[]
for list_item in last_links_item:								# filtering the links for only https url
	links.append(list_item.get('href'))


f = csv.writer(open('Company.csv', 'w'))						# Creating the CSV file to stor data in write mode
f.writerow(['Name of Company', 'Contact Name','Designation','Street Adress','City','State','Pincode','Email','Phone','Mobile','Website'])
																# Added the Column names for formatting the data
for urlLink in links:											# main loop for data extraction 
	page=requests.get(urlLink)
	soup=BeautifulSoup(page.text, 'html.parser')
	post=soup.find_all(class_="post-content")
	try:
		post=post[3].find_all('p')
		print(post[0].contents[1])
		try:
			nameOfCompany=post[0].contents[1]
			contactName=post[1].contents[1]
			designation=post[2].contents[1]
			streetAddress=post[3].contents[1]
			city=post[4].contents[1]
			state=post[5].contents[1]
			pincode=post[6].contents[1]
			email=post[7].contents[1]
			phone=post[8].contents[1]
			mobile=post[9].contents[1]
			web=post[10].contents[1]

		except IndexError:
			continue
	except IndexError:
		continue

	f.writerow([nameOfCompany,contactName,designation,streetAddress,city,state,pincode,email,phone,mobile,web])  # writing the data to CSV file 


