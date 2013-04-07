import random, string

from flask import Blueprint
from database import db

app = Blueprint('simpleblog',
				__name__, 
				template_folder='templates', 
				url_prefix='/blog')

