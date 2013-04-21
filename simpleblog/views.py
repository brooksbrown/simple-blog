import random, string, datetime, os

from flask import Blueprint, render_template, request, redirect, send_from_directory
from werkzeug import secure_filename

from database import db

from forms import NewTextBlogForm, NewPhotoBlogForm, NewQuoteBlogForm, NewVideoBlogForm, NewAudioBlogForm, NewLinkBlogForm
from models import BlogEntry, BlogTag, BlogEntryPhoto
from config import UPLOAD_PATH 

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
		new_blog = create_blog(form.title.data, form.tags.data, form.body.data, form.post_submit.data)
		return redirect("/")
	return render_template('simpleblog/text-new.html', form=form)	

@app.route('/photo/new', methods=['GET', 'POST'])
def new_photo_blog():
	form = NewPhotoBlogForm()
	form.enctype = 'enctype=multipart/form-data'

	if request.method == 'POST' and form.validate():
		new_blog = create_blog(form.title.data, form.tags.data, form.body.data, form.post_submit.data)
		new_blog_data = BlogEntryPhoto()
		new_blog_data.blog_entry_id = new_blog.id
		
		photo_file = request.files['file']
		if photo_file:
			filename = secure_filename(photo_file.filename)
			photo_file.save(os.path.join(UPLOAD_PATH, filename))
			new_blog_data.photo_file = filename
		new_blog_data.photo_link = form.link.data
		new_blog.blog_type = 'photo'
		db.session.add(new_blog_data)
		db.session.commit()
		return redirect('/')

	return render_template('simpleblog/photo-new.html', form=form)

@app.route('/quote/new')
def new_quote_blog():
	form = NewQuoteBlogForm()

	if request.method == 'POST' and form.validate():
		new_blog = create_blog(form.title.data, form.tags.data, form.body.data, form.post_submit.data)
		new_blog_data = BlogEntryQuote()
		new_blog_data.blog_entry_id = new_blog.id
		new_blog_data.quote = form.quote.data
		new_blog_data.source = form.source.data
		new_blog.blog_type = 'quote'
		db.session.add(new_blog_data)
		db.session.commit()
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
			blogs.append(render_template('simpleblog/text-view-listing.html', blog=blog))
		elif blog.blog_type == 'photo':
			blog_photo = BlogEntryPhoto.query.filter_by(blog_entry_id=blog.id).first()
			if blog_photo.photo_link is not None:
				blog.photo = blog_photo.photo_link
			if blog_photo.photo_file is not None:
				blog.photo = '/blog/uploads/' + blog_photo.photo_file
			blogs.append(render_template('simpleblog/photo-view-listing.html', blog=blog))

	return render_template('simpleblog/blog-list.html', blogs=blogs)

# tags should be a comma delimited string
def create_blog(title, tags, body, published_flag):
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
	new_blog.published = published_flag
	db.session.add(new_blog)
	db.session.commit()
	return new_blog

def file_ext_check(filename, allowed_extensions):
	return '.' in filename and filename.rsplit('.',1)[1] in allowed_extensions

