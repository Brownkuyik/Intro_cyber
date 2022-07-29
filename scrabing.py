from nturl2path import url2pathname
from bs4 import BeautifulSoup
import requests


url = "https://web.facebook.com/?_rdc=1&_rdr"
r = requests.get(url)


soup = BeautifulSoup(r.content, 'html5lib')
m = soup.prettify() #this is to get all the information about the site.
p = soup.p #to get all the paragraph tag
t = soup.title #to get the site title
a = soup.a #to get a link tag on a website
v = soup.video # to get video that are on the site your looking at
m = soup.img #used to obtain image from a site for you used


"""to fine something on a site"""
w = soup.find('button')
al = soup.find_all('button')
"""to fine different all in different task, used a list to mention the name of what you fave to fine [] example below"""
al_list = soup.find_all(['button', 'img'])
# print(al_list)

'''to change the value or make temporarty  changes on a site'''
ta = soup.button
# print(ta.attrs['name'])
# o = ta.attrs['name'] = 'log_out'
# print('new one', o)

'''using an append to add another thing to the already included value of something and include another on that place'''
print(ta.string)
print(ta.append('HOME'))
print('update....', ta.contents)

'''to clear all the items on a website using .clear method'''
print(ta.clear())
print('updated...',ta.contents)
print(soup.original_encoding)


'''to get the name of all the task that made up a web site'''
# mine = soup.find_all(True)
# for k in mine:
#     print(k.name)




""" To made the change in a server to remain permanently we use pen testing server"""


