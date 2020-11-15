import requests
from bs4 import BeautifulSoup
import json
def article_collecter(url):

	#url = 'https://www.opportunitiesforafricans.com/daad-in-region-scholarship-programme-call-for-scholarship-applications-2021/'
	r = requests.get(url)
	html_contents = r.text
	html_soup = BeautifulSoup(html_contents, 'html.parser')
	article = html_soup.find('article')


	#print title of scholarship
	article_details = []
	article_details.append(article.find(class_ = 'entry-title').text)
	#find date uploaded
	article_details.append(f'date announced:{article.find(class_="entry-date updated td-module-date").text}')
	#to get scholarship deadline
	article_details.append(article.find('p').text)

	#this removes all the script tags
	list_of_script = [x.extract() for x in article.findAll('script')]
	list_of_style = [x.extract() for x in article.findAll('style')]

	article = article.find(class_ = 'td-post-content tagdiv-type')
	'''
	for string in article.strings:
		print (string)
	'''
	article_list = article.strings
	article = list(article_list)
	while'\n' in article:
	
		article.remove('\n')
	article = [article_details,article]
	article.append(f'url : {url}')
	#article_details.append(article)	
	return(article)
def links_extractor(pg_number):
	url = f'https://www.opportunitiesforafricans.com/category/scholarships/page/{pg_number}/'
	r = requests.get(url)
	html_contents = r.text
	html_soup = BeautifulSoup(html_contents, 'html.parser')	
	links = html_soup.find(class_ = 'td-ss-main-content')
	list_of_authors = [x.extract() for x in links.findAll(class_="td-post-author-name")]
	list_of_links = [x.extract() for x in links.findAll('a',href = True)]
	#print(links.find_all(href = True))
	links = []
	for link in list_of_links:
		links.append(link['href'])
	link_set = set(links)
	links = list(link_set)
	for link in link_set:
		if ('#respond' in link):
			links.remove(link)
		elif ('#comments' in link):
			links.remove(link)
		elif ('category/' in link):
			links.remove(link)
		elif ('/page/' in link):
			links.remove(link)
			
	return links
		


reject = []
for i in range(6,38):
	scholarships = []
	print(i)
	links = links_extractor(i)
	for url in links:
		print(url)
		try:
			article = article_collecter(url)
			scholarships.append(article)
		except:
			reject.append(url)
	file = f'scholarship_page_{i}.json'		
	with open(file,'w') as f:
		json.dump(scholarships, f)

		


print(f'{len(reject)} was rejected')
print(reject)