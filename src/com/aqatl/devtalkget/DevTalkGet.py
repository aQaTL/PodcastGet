import os
import feedparser
from sys import exit

dtUrl = "http://feeds.feedburner.com/devtalk_pl?format=xml"
dt = feedparser.parse(dtUrl)
epUrl = dt.entries[0].media_content[0]["url"]
epName = epUrl[34:]
os.chdir("E:\Music\Podcasty\DevTalk")

if epName in os.listdir(os.curdir):
    exit(0)
else:
    os.system("wget " + epUrl + " -O " + epName)


