from bs4 import BeautifulSoup
import pandas as pd
import requests

flipkart_phones = {}
names_list = []
prices_list = []
speci_list = []


for page in range (1,11):
    url_2 = f'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}'
    html_code = requests.get(url_2).content
    # print(html_code)
    soup = BeautifulSoup(html_code, 'lxml')
    # print(soup.prettify())
    phones = soup.find_all('div', class_ = '_3pLy-c row')
    for phone in phones:
        
        names = phone.find('div', class_ = '_4rR01T').get_text()
        prices = int(phone.find('div', class_ = '_30jeq3 _1_WHN1').get_text().replace('₹','').replace(',',''))
        Speci = phone.find('ul', class_ = '_1xgFaf').get_text()


            

      
        names_list.append(names)
        prices_list.append(prices)
        speci_list.append(Speci)
       
    
flipkart_phones['names'] = names_list
flipkart_phones['prices'] = prices_list
flipkart_phones['specifications'] = speci_list


# print(flipkart_phones)

file = pd.DataFrame(flipkart_phones, columns = ['names', 'prices','specifications'])

# print(file)
file.to_csv('Flipkart phones Details.csv')