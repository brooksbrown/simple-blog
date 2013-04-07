import random, string

from flask import Blueprint, render_template
from database import db

from forms import NewTextBlogForm

app = Blueprint('simpleblog',
				__name__, 
				template_folder='templates', 
				url_prefix='/blog')


@app.route('/text/new')
def new_blog():
	form = NewTextBlogForm()
	return render_template('simpleblog/text-new.html', form=form)	
