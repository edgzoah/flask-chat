from lib import *
from app import *
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'F3HUIF23H8923F9H8389FHXKLN'

# socketio = SocketIO(app, cors_allowed_origins='*')


# login_manager = LoginManager()
# login_manager.login_view = "login"
# login_manager.init_app(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/chat'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

# arr = [users('edgzoah', 'adamoblady@gmail.com', 'dobra123'), users('wiejak', 'wiejakkrul@gmail.com', '12345678')]
# for i in arr:
#   db.session.add(i)
#   db.session.commit()

l = [chat(1, 2, 'guwno'), chat(1, 2, 'sraka')]
for i in l:
  db.session.add(i)
  db.session.commit()

# create tables
# db.create_all()