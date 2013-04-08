import random, string

from flask import Blueprint, render_template
from database import db

from forms import NewTextBlogForm, NewPhotoBlogForm, NewQuoteBlogForm

app = Blueprint('simpleblog',
				__name__, 
				template_folder='templates', 
				url_prefix='/blog')


@app.route('/text/new')
def new_text_blog():
	form = NewTextBlogForm()
	return render_template('simpleblog/text-new.html', form=form)	

@app.route('/photo/new')
def new_photo_blog():
	form = NewPhotoBlogForm()
	return render_template('simpleblog/photo-new.html', form=form)

@app.route('/quote/new')
def new_quote_blog():
	form = NewQuoteBlogForm()
	return render_template('simpleblog/quote-new.html', form=form)




