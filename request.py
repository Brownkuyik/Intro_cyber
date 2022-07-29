import requests
from bs4 import BeautifulSoup


ur = 'https://web.facebook.com/?_rdc=1&_rdr'
new_url = {'home':'brown', 'html':'kuyik', 'get':'olalalla'}
#another link or url can be added to a sit using request
m = requests.get(ur, new_url)
# print(m.url)
"""to get the headers of a site"""
r = requests.get(ur)
#r.headers
#To get the text in a side
#r.text

"""TO get some img or information that request cant prived, 
# we use beautiful soup to access them"""

# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.img)
# """TO get to the url of the image or video  and send a request to get it down to your system"""
image = requests.get("https://static.xx.fbcdn.net/rsrc.php/y8/r/dF5SId3UHWd.svg")

#To write to a file in the system
'''the r is used as a reject expression so that it wont go out og expectation'''
with open(r'C:/Users/kuyik/Pictures/Camera Roll/name.svg', 'wb') as files:  #the last sladge is used to change the name to what you want but remember to used the same name as the files you want
    files.write(image.content)
    print('image gotten')

