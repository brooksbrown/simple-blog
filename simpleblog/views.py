import random, string

from flask import Blueprint, render_template
from database import db

from forms import NewTextBlogForm, NewPhotoBlogForm, NewQuoteBlogForm, NewVideoBlogForm, NewAudioBlogForm, NewLinkBlogForm

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
	form = NewVideoBlogForm()
	return render_template('simpleblog/video-new.html', form=form)

@app.route('/audio/new')
def new_audio_blog():
	form = NewAudioBlogForm()
	return render_template('simpleblog/audio-new.html', form=form)

@app.route('/link/new')
def new_link_blog():
	form = NewLinkBlogForm()
	return render_template('simpleblog/link-new.html', form=form)


