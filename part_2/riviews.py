# import requests, csv
# from bs4 import BeautifulSoup
#
# html_doc = requests.get('https://id.carousell.com/kiyowoshop/reviews/')
# soup = BeautifulSoup(html_doc.text, 'html.parser')
#
# riviews = soup.find(attrs={'class':'_13w_InnkzD'})
#
# titles = riviews.findAll(attrs={'class':'_1hkYwIYLT6'})
#
# file = open('hasilriviews.csv', 'w', newline='')
# writer = csv.writer(file)
# headers = ['Username', 'Day', 'Riviews']
# writer.writerow(headers)
#
# for title in titles:
#     username = title.find('span', attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _1avuYeUOLe _3k5LISAlf6'}).text
#     day = title.find('span', attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA _2m1WFlGyTw lqg5eVwdBz _19l6iUes6V _30RANjWDIv'}).text
#     riviews = title.find('p', attrs={'class':'_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA _2m1WFlGyTw lqg5eVwdBz _19l6iUes6V _3vlPf4XcxN _3k5LISAlf6'}).text
#     print(username, day, riviews)
#     file = open('hasilriviews.csv', 'a', newline='', encoding='utf-8')
#     writer = csv.writer(file)
#     writer.writerow([username, day, riviews])
#     file.close()
#
#


import requests
import random
import csv
import concurrent.futures

#opens a csv file of proxies and prints out the ones that work with the url in the extract function

proxylist = []

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
        print(r.json(), ' | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)