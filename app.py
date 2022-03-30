from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def main():
  return render_template('index.html')

@socketio.on('message')
def handlemsg(msg):
  socketio.send(msg, brodcast=True)
  



if __name__ == '__main__':
	socketio.run(app)