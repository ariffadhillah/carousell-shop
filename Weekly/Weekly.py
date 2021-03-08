from pip._vendor.contextlib2 import redirect_stderr
from requests_html import HTMLSession
import chompjs

s = HTMLSession()
url = 'https://www.rei.com/c/hiking-backpacks?page=1'
baseurl = 'https://www.rei.com'
r = s.get(url)

results = r.html.find('#search-results > ul > li > a')

# print(results)



# for link in results:
#     print(baseurl + link.attrs['href'])


produckslinks = []

for link in results:
    produckslinks.append(baseurl + link.attrs['href'])

links = list(dict.fromkeys(produckslinks))

print(links)