import urllib, urllib2, json


def reddit(searchy):
	url = "http://www.reddit.com/search.json?q=" + searchy
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	values = {'name': 'Rei Ayanami', 'location': 'Neo-Tokyo','language': 'Python' }
	headers = {'User-Agent': user_agent}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	the_page = response.read()
	jsonified_item = json.loads(the_page)
	rlist = []

	for i in range(10):
		subreddit = jsonified_item['data']['children'][i]['data']['subreddit_name_prefixed']
		title = jsonified_item['data']['children'][i]['data']['title']
		rurl = jsonified_item['data']['children'][i]['data']['url']
		rlist.extend([subreddit,title,rurl])
		#relem = "[%s] %s \n %s \n\n" % (subreddit, title, rurl)
		#rlist.append(relem)
		
	return rlist
