import random, string, datetime

from flask import Blueprint, render_template, request, redirect
from database import db

from forms import NewTextBlogForm, NewPhotoBlogForm, NewQuoteBlogForm, NewVideoBlogForm, NewAudioBlogForm, NewLinkBlogForm
from models import BlogEntry, BlogTag

app = Blueprint('simpleblog',
				__name__, 
				template_folder='templates', 
				url_prefix='/blog')


@app.route('/text/new', methods=['GET', 'POST'])
def new_text_blog():
	form = NewTextBlogForm()

	if request.method == 'POST' and form.validate():

		new_blog = create_blog(form.title.data, form.tags.data, form.body.data)
		return redirect("/")
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




# tags should be a comma delimited string
def create_blog(title, tags, body):
	new_blog = BlogEntry()
	new_blog.title = title

	tags = tags.split(',')
	tag_objects = []
	for tag in tags:
		storedTag = BlogTag.query.filter_by(title=tag).first()
		if storedTag == None:
			storedTag = BlogTag()
			storedTag.title = tag
			db.session.add(storedTag)
			db.session.commit()
		tag_objects.append(storedTag)
	new_blog.tags = tag_objects
	new_blog.body = body
	new_blog.created = new_blog.updated = datetime.datetime.now()
	db.session.add(new_blog)
	db.session.commit()
