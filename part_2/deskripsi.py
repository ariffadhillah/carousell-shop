import requests, csv
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/home-and-gardening-13/')
soup = BeautifulSoup(html_doc.text, 'html.parser')

camera_terpopuler = soup.find(attrs={'class': '_2RJeLsMmpi'})

titles = camera_terpopuler.findAll(attrs={'class': 'TpQXuJG_eo'})

file = open('hasildeskripsi.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Nama Produck', 'Deskripsi Produck']
writer.writerow(headers)

for title in titles:
    # deskripsi barang
    deskripsi_produck = (title.find('p', attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv'}).text)
    nama_produck = (title.find('p', attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)

    file = open('hasildeskripsi.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ['Nama Produck', 'Deskripsi Produck']
    writer.writerow([nama_produck, deskripsi_produck])
    file.close()











