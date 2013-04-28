import random, string, datetime, os

from flask import Blueprint, render_template, request, redirect, send_from_directory
from werkzeug import secure_filename

from database import db

from forms import NewTextBlogForm, NewPhotoBlogForm, NewQuoteBlogForm, NewVideoBlogForm, NewAudioBlogForm, NewLinkBlogForm
from models import BlogEntry, BlogTag, BlogEntryPhoto
from config import UPLOAD_PATH 
from utilities import create_blog_tag, blog_create, blog_photo_create, blog_quote_create

app = Blueprint('simpleblog',
				__name__, 
				template_folder='templates', 
				url_prefix='/blog')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	    return send_from_directory(UPLOAD_PATH, filename)

@app.route('/text/new', methods=['GET', 'POST'])
def new_text_blog():
	form = NewTextBlogForm()

	if request.method == 'POST' and form.validate():
		new_blog = blog_create(form.title.data, form.tags.data, form.body.data, form.post_submit.data)
		new_blog.blog_type = 'text'
		db.session.commit()
		return redirect("/")
	return render_template('simpleblog/text-new.html', form=form)	

@app.route('/<blog_id>/edit', methods=['GET', 'POST'])
def edit_blog(blog_id):
	blog = BlogEntry.query.filter_by(id=blog_id).first()
	if blog.blog_type == 'text':
		form = NewTextBlogForm()
		form.title.data = blog.title
		for tag in blog.tags:
			print "###############"
			print tag.title
		form.body.data = blog.body
		
		if request.method == 'POST' and form.validate():
			blog.title = form.title.data
			tags = form.tags.data.split(',')
			tag_objects = []
			for tag in tags: 
				storedTag = BlogTag.query.filter_by(title=tag).first()
				tag_objects.append(storedTag)
			blog.tags = tag_objects
			db.session.commit()	
			return redirect("/")
		return render_template('simpleblog/text-new.html', form=form)	
	return redirect('/')

@app.route('/photo/new', methods=['GET', 'POST'])
def new_photo_blog():
	form = NewPhotoBlogForm()
	form.enctype = 'enctype=multipart/form-data'

	if request.method == 'POST' and form.validate():
		new_blog = blog_create(form.title.data, form.tags.data, form.body.data, form.post_submit.data)
		new_blog_photo = blog_photo_create(new_blog, form.link.data, request.files['file'])
		return redirect('/')

	return render_template('simpleblog/photo-new.html', form=form)

@app.route('/quote/new')
def new_quote_blog():
	form = NewQuoteBlogForm()

	if request.method == 'POST' and form.validate():
		new_blog = blog_create(form.title.data, form.tags.data, form.body.data, form.post_submit.data)
		new_blog_quote = blog_quote_create(new_blog, form.quote.data, form.source.data)
		return redirect('/')

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


@app.route('/list')
def blog_list():
	blogs = []
	for blog in BlogEntry.query.all():
		if blog.blog_type == 'text':
			blog.edit_link = '<a href="/blog/' + str(blog.id) + '/edit">edit</a>'
			blogs.append(render_template('simpleblog/text-view-listing.html', blog=blog))
		elif blog.blog_type == 'photo':
			blog_photo = BlogEntryPhoto.query.filter_by(blog_entry_id=blog.id).first()
			if blog_photo.photo_link is not None:
				blog.photo = blog_photo.photo_link
			if blog_photo.photo_file is not None:
				blog.photo = '/blog/uploads/' + blog_photo.photo_file
			blogs.append(render_template('simpleblog/photo-view-listing.html', blog=blog))

	return render_template('simpleblog/blog-list.html', blogs=blogs)


def file_ext_check(filename, allowed_extensions):
	return '.' in filename and filename.rsplit('.',1)[1] in allowed_extensions

