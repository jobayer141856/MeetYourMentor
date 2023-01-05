from random import randint
from flask import *
from flask_mail import *
import bcrypt
import pymongo

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL= True
MAIL_USERNAME = 'meetyourmentor150@gmail.com'
MAIL_PASSWORD = 'fkffwsdunbvbqonc'

db_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = db_client["users"]

db_std = db.std_info
db_mentor = db.mentor_info
db_mentor_academic = db.mentor_academic_info
db_mentor_dashboard = db.mentor_dashboard
db_std_dashboard = db.std_dashboard
db_std_thoughts = db.std_thoughts
db_mentor_thoughts = db.mentor_thoughts
db_post_for_mentor = db.request_for_mentor

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

app.secret_key = "testing"

from app.routes import login
from app.routes import forgot
from app.routes import home
from app.routes import register
from app.routes import howitwork
from app.routes import logout
from app.routes import verify
from app.routes import mentorprofile
from app.routes import change_pass
from app.routes import academic_mentor
from app.routes import stdprofile
from app.routes import findmentor
from app.routes import requestmentor
from app.routes import stdpost
from app.routes import postformentor
from app.routes import findstudents
from app.routes import requeststudent

