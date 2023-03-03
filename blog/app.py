from datetime import datetime

from flask import Flask, request, g

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/greet/<name>/')
def greet_name(name: str):
    return f'Hello, {name}'


@app.route('/user/')  # /?name=name&surname=srname
def read_user():
    name = request.args.get('name')
    surname = request.args.get('surname')
    return f'User {name or "[noname]"} {surname or "[nosurname]"} is collected.'


@app.route('/status/', methods=['GET', 'POST'])
def custom_status_code():
    if request.method == 'GET':
        return 'To get response with custom status code send request using POST method and pass ' \
               '`code` in JSON body / FormData'

    print('raw bytes data:', request.data)
    if request.form and 'code' in request.form:
        return 'code from form', request.form['code']

    if request.json and 'code' in request.json:
        return 'code from json', request.json['code']

    return '', 204

"""
@app.before_request
def process_before_request():
    # замеряеми время обработки
    g.start_time = datetime.now()

@app.after_request
def process_after_request(response):
    if hasattr(g, 'start_time'):
        time_start = datetime(g.start_time)
        time_now = datetime.now()
        response.headers['process-time'] = time_now - time_start
    return response
"""