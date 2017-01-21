import os
import feedparser
import configparser

config = configparser.ConfigParser()
config.read('../../../../config.ini')

for item in config["PODCASTS"].items():
    print("Searching for new " + item[0] + " episode")
    podcastFeed = feedparser.parse(item[1])
    epFeed = podcastFeed.entries[0]
    epUrl = epFeed.enclosures[0]["href"]
    epFilename = "\"" + epFeed.title + os.path.splitext(epUrl)[1] + "\""
    folderPath = config["PATHS"]["DefaultPath"] + item[0]
    try:
        os.chdir(folderPath)
    except FileNotFoundError:
        os.mkdir(folderPath)
        os.chdir(folderPath)

    if epFilename[1:-1] not in os.listdir(os.curdir):
        print("Started downloading " + epFilename + " from " + item[0] + "\n")
        os.system("wget " + epUrl + " -O " + epFilename)
        print(epFilename + " has been downloaded into " + folderPath)
    else:
        print("Nothing new here")
