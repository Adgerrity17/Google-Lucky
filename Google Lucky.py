#Im feeling lucky google search
#opens several google search results

import requests, sys, webbrowser, bs4
#need to import / pip install requests and bs4

print('Googling...') #desplay text while downloading the google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
LinkElems = soup.select('.r a')
numopen = min(5, len(LinkElems))
for i in range(numopen):
    webbrowser.open('http://google.com' + LinkElems[i].get('href'))
    