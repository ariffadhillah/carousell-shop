# import requests
# from bs4 import BeautifulSoup
#
# html_doc = requests.get('https://id.carousell.com/categories/photography-6/')
# soup = BeautifulSoup(html_doc.text, 'html.parser')
#
# camera_terpopuler = soup.find(attrs={'class': '_2RJeLsMmpi'})
#
# titles = camera_terpopuler.findAll(attrs={'class': 'TpQXuJG_eo'})
#
# for title in titles:
#     # title text
#     print(title.find('p', attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
#     # image
#     print( title.find('span', attrs={'class': '_3nH6adLACP _3k9K3fuPdS _14ECgRVNZW'}).find('img')['src'] )
#     # harga
#     print(title.find('p', attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).text)
#
#


import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures

#get the list of free proxies
def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies

def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
        print(r.json(), r.status_code)
    except:
        pass
    return proxy

proxylist = getProxies()
#print(len(proxylist))

#check them all with futures super quick
with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)

# req = Request('https://duradek.com/', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# print(webpage)