from flask import Flask , request , abort , redirect , Response ,url_for, render_template, flash
from flask_socketio import SocketIO, send
from flask_login import LoginManager, login_required, UserMixin, login_user, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import pymysql