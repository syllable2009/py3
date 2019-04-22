
#http://docs.jinkan.org/docs/flask/quickstart.html#quickstart
from flask import Flask,jsonify
#jsonify不仅会将内容转换为json，而且也会修改Content-Type为application/json
app = Flask(__name__)

@app.route('/')
def index():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')