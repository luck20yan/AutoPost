from flask import Flask, request
import config
from autopost import Post
app = Flask(__name__)


@app.route('/vk')
def hello_world():
    data = request.get_json()
    print(data)


if __name__ == '__main__':
    app.run()
