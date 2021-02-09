import autopost
post = autopost.Post("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non mi tristique, consectetur dui eu, tempus sapien. Phasellus tincidunt eu augue ut pulvinar.
""", ['img/image.jpg', 'img/image2.jpg'])
post.send_twitter()
