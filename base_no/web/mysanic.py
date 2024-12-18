from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

@app.route('/')
def index(request):
    return text('Index Page')

@app.route('/hello')
def hello(request):
    return text('Hello World')

@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))

@app.route('/person/<name:[A-z]>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))

app.run(host="0.0.0.0", port=9090, debug=False)

