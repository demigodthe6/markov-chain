import urllib2

response = urllib2.urlopen('http://www.gutenberg.org/files/135/135-h/135-h.htm')
html = response.read()
sad = 0

list_of_words = html.split(' ')

for word in list_of_words:
	if word == 'sad':
		sad += 1

print sad