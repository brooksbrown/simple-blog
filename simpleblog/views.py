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

@app.route('/video/new')
def new_video_blog():
	form = NewQuoteVideoForm()
	return render_template('simpleblog/quote-new.html', form=form)

@app.route('/audio/new')
def new_audio_blog():
	form = NewQuoteAudioForm()
	return render_template('simpleblog/quote-new.html', form=form)

@app.route('/link/new')
def new_link_blog():
	form = NewQuoteLinkForm()
	return render_template('simpleblog/quote-new.html', form=form)


