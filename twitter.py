import tweepy

import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)
tweet = "Text part of the tweet"  # toDo
image_path = "./img/image.jpg"  # toDo


def send_tweet_text(text):
    api.update_status(status=text)


def send_tweet_with_images(text, images):
    media_ids = [api.media_upload(i).media_id_string for i in images]
    api.update_status(text, media_ids=media_ids)
