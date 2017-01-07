import os
import feedparser
import configparser

def getFileName(url):
    urlChunks = url.split('/')
    return urlChunks[len(urlChunks) - 1]


config = configparser.ConfigParser()
config.read('../../../../config.ini')

for item in config["PODCASTS"].items():
    podcastFeed = feedparser.parse(item[1])
    epUrl = podcastFeed.entries[0].media_content[0]["url"]
    epName = getFileName(epUrl)
    folderPath = config["PATHS"]["DefaultPath"] + item[0]
    try:
        os.chdir(folderPath)
    except FileNotFoundError:
        os.mkdir(folderPath)
        os.chdir(folderPath)

    if epName not in os.listdir(os.curdir):
        os.system("wget " + epUrl + " -O " + epName)
