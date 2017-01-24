import os
import feedparser
import configparser
import sys


def downloadEp(epVendor, epUrl, epFilename, folderPath):
	if epFilename[1:-1] not in os.listdir(os.curdir):
		print("Started downloading " + epFilename + " from " + epVendor + "\n")
		os.system("wget " + epUrl + " -O " + epFilename)
		print(epFilename + " has been downloaded into " + folderPath)


config = configparser.ConfigParser()
config.read('../../../../config.ini')

for idx, item in enumerate(config["PODCASTS"].items()):
	print("Searching for " + item[0])
	podcastFeed = feedparser.parse(item[1])

	folderPath = config["PATHS"]["DefaultPath"] + item[0]
	try:
		os.chdir(folderPath)
	except FileNotFoundError:
		os.mkdir(folderPath)
		os.chdir(folderPath)

	try:
		all = sys.argv[1] == "-a"
		epNum = int(sys.argv[2])
	except (ValueError, IndexError):
		all = False

	if all and epNum == idx:
		for entry in podcastFeed.entries:
			epUrl = entry.enclosures[0]["href"]
			downloadEp(
				item[0],
				epUrl,
				"\"" + entry.title + os.path.splitext(epUrl)[1] + "\"",
				folderPath)
	else:
		epUrl = podcastFeed.entries[0].enclosures[0]["href"]
		downloadEp(
			item[0],
			epUrl,
			"\"" + podcastFeed.entries[0].title + os.path.splitext(epUrl)[1] + "\"",
			folderPath)
