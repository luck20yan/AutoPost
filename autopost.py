import telegram
import twitter


class Post:
    def __init__(self, text: str, images: list):
        self.text: str = text
        self.images: list = images

    def send_telegram(self):
        telegram.send_post(self.text, self.images)

    def send_twitter(self):
        if len(self.text) > 255:
            raise Exception(f'Tweet len needs to be < 255. but now {len(self.text)}')
        if len(self.images) == 0:
            twitter.send_tweet_text(self.text)
        else:
            twitter.send_tweet_with_images(self.text, self.images)