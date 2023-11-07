import feedparser
from datetime import datetime
from discord_webhook import DiscordWebhook
import configparser
import schedule
import time

def convert2time(stringtime):
    # "2023-11-02T16:11:32+00:00"
    return datetime.strptime(stringtime.replace("T", " ").split("+")[0], '%Y-%m-%d %H:%M:%S')

def check_ytchannel(ytchannel_id='', webhook_url='', word=''):
    print("Checking the channel: " + ytchannel_id)
    config = configparser.ConfigParser()
    config.read('config.ini')

    url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + ytchannel_id
    feed_update = feedparser.parse(url)
    #print(feed_update.get('entries'))

    try:
        current = config['DEFAULT'][ytchannel_id]
    except:
        # config doesn't exist, create one
        print('Create config...')
        current = '2023-11-02T16:31:47+00:00'
        config['DEFAULT'][ytchannel_id] = current
        with open('config.ini', 'w') as configfile:
           config.write(configfile)

    for video in feed_update.get('entries'):
        title = video.get('title')
        link = video.get('link')
        published = video.get('published')
        if convert2time(published) > convert2time(current):
            if word in title:
                print(title + " " + link + " " + published)
                thread_name = title
                message = link
                webhook = DiscordWebhook(url=webhook_url, content=message, thread_name=thread_name)
                response = webhook.execute()
        else:
            print("No update...")
            break
    # store the published time of the newest video
    config['DEFAULT'][ytchannel_id] = feed_update.get('entries')[0].get('published')
    with open('config.ini', 'w') as configfile:
      config.write(configfile)
