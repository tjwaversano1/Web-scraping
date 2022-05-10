from bs4 import BeautifulSoup
import requests
from csv import writer
url = "https://www.har.com/trending_for__rent"
page = requests.get(url)
print(page)

soup = BeautifulSoup (page.content, 'html.parser')
lists = soup.find_all('div', class_='prop_item status-active')

with open ('housing.csv','w', encoding='utf8', newline ='') as f:
    thewriter = writer(f)
    header = ['Address','Features']
    thewriter.writerow(header)

    for list in lists:
        address= list.find('a', class_='address').text.replace('/n','')
        features = list.find('div', class_='mpf_item show_resp').text.replace('/n', '')
        info = [address, features]
        thewriter.writerow(info)
