import urllib
page =urllib.urlopen('http://www.baidu.com')
print(page.read())