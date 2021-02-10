import requests
from bs4 import BeautifulSoup


def ouo(url):
	key = url.split('/')[-1]
	main = 'https://ouo.io/'
	
	with requests.Session() as s:
		s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101'})
		
		
		first = s.get(main + key, allow_redirects=False)
		soup = BeautifulSoup(first.text, 'html.parser')
		data = {'_token': soup.find('input', attrs={'name':'_token'})['value']}
		s.headers.update({'referer': first.url})
		
		
		
		second = s.post(main + 'go/' + key, data=data, allow_redirects=False)
		soup = BeautifulSoup(second.text, 'html.parser')
		data = {'_token': soup.find('input', attrs={'name':'_token'})['value']}
		s.headers.update({'referer': second.url})
		
		
		return(s.post(f'https://ouo.io/xreallcygo/{key}', data=data).url)


print(ouo('your ouo.io link here'))