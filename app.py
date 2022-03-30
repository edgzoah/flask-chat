from lib import *
from model import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F3HUIF23H8923F9H8389FHXKLN'

socketio = SocketIO(app, cors_allowed_origins='*')


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/chat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

x = ''

@login_manager.user_loader
def load_user(user_id):
    return users.query.filter_by(id=user_id).first()

@app.route('/login' , methods=['GET' , 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect('/')
  if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      registeredUser = users.query.filter_by(username=username, password=password).first()
      if registeredUser:
          login_user(registeredUser)
          return redirect('/')
      else:
          flash('Incorrect username or password')
          return redirect('/login')
  return render_template('login.html')

@app.route('/')
def index():
  return render_template('main.html')

@app.route('/msg')
@login_required
def main():
  global x
  if request.args['user']:
    if request.args['user'] != '':
      if db.session.query(users.username).filter(users.username == request.args['user']).first():
        x = request.args['user']
        q = db.session.query(users.id).filter(users.username == current_user.username).first()
        q1 = db.session.query(users.id).filter(users.username == x).first()
        q2 = db.session.query(chat.message).filter(chat.sender == q[0] and chat.receiver == q1[0]).all()
        q3 = db.session.query(chat.message).filter(chat.sender == q1[0] and chat.receiver == q[0]).all()
        # print(q2)
        # q1 = db.session.query(chat.message, users.username).filter(users.id == chat.receiver).first()
        return render_template('index.html', receiver=request.args['user'])
      else: return redirect('/')
    else: return redirect('/')
  else: return redirect('/')

@socketio.on('message')
def handlemsg(msg):
  global x
  print(x)
  try:
    socketio.send(current_user.username + ' - ' + msg, brodcast=True)
  except:
    return redirect('/')

if __name__ == '__main__':
	socketio.run(app)