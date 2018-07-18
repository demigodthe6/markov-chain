import urllib2
from bs4 import BeautifulSoup

def get_data():
	site = raw_input('Enter lyric url here(azlyrics only): ')
	page = urllib2.urlopen(site)
	html_doc = page.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	a = soup.find_all('div')
	for div in a:
		if div.has_attr('class') == False and div.has_attr('id') == False:
			return div.get_text().encode('UTF-8')