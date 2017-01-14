# PodcastGet
Simple python app that downloads new episodes of your favourites podcasts using RSS feeds

## Installation

Before installation, make sure that your setup matches the [requirements](#requirements).

1. Clone this repo `git clone https://github.com/aQaTL/PodcastGet.git` or download it as zip and unpack it.
2. Cd into it `cd PodcastGet`.
3. Create config file `config.ini` (see the [Creating config file](#creating-config-file) section).
4. Now you can run it by cd'ing into `src/com/aqatl/podcastget` and typing `python PodcastGet.py`.
5. I recommend adding `podcastget` folder to your PATH variable, so you can run this app without cd'ing into repo every time you want to use it.

## Requirements

- [Python 3](https://www.python.org/) programming language (tested with version 3.6)
- [feedparser](https://pypi.python.org/pypi/feedparser) python library (tested with version 5.2.1)

## Creating config file

The default filename is `config.ini`, which you can change in the python script. After that fill the file using pattern shown below.
```
[PATHS]
DefaultPath = path_to_your_podcasts_folder

[PODCASTS]
podcast_name = rss_feed_address
podcast2_name = rss_feed_address2
```
Tip: I recommend adding `?format=xml` suffix to the rss feed address