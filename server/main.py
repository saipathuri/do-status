from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
sio = SocketIO(app)

last_known_data = None

@app.route('/')
def index():
    global last_known_data
    return last_known_data

@sio.on('data')
def event(data):
    global last_known_data
    last_known_data = data
    sio.emit('ui_data', {'data': 'foobar'})

if __name__ == '__main__':
    print("starting server")
    sio.run(app, host='0.0.0.0', port='5000', debug=True, use_reloader=True)