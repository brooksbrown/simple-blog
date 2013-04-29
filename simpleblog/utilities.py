import datetime

from database import db
from models import *

# tags should be a comma delimited string
def blog_create(title, tags, body, published_flag):
	new_blog = BlogEntry()
	new_blog.title = title

	tags = tags.split(',')
	tag_objects = []
	for tag in tags:
		storedTag = create_blog_tag(tag)
		tag_objects.append(storedTag)
	new_blog.tags = tag_objects
	new_blog.body = body
	new_blog.created = new_blog.updated = datetime.datetime.now()
	new_blog.published = published_flag

	db.session.add(new_blog)
	db.session.commit()
	return new_blog

def	blog_photo_create(blog, photo_link, photo_file = None):
	blog_photo = BlogEntryPhoto()
	blog_photo.blog_entry_id = blog.id

	if photo_file:
		filename = secure_filename(photo_file.filename)
		photo_file.save(os.path.join(UPLOAD_PATH, filename))
		blog_photo.photo_file = filename
	blog_photo.photo_link = photo_link 
	blog.blog_type = 'photo'
	db.session.add(blog_photo)
	db.session.commit()
	return blog_photo

def blog_quote_create(blog, quote, source):
	blog_quote = BlogEntryQuote()
	blog_quote.blog_entry_id = blog.id
	blog_quote.quote = quote
	blog_quote.source = source
	blog.blog_type = 'quote'
	db.session.add(blog_quote)
	db.session.commit()
	return blog_quote

#	if tag exists it is returned
#	if not it will be created and returned
def create_blog_tag(tag_title):
	tag = BlogTag.query.filter_by(title=tag_title).first()
	if tag == None:
		tag = BlogTag()
		tag.title = tag_title
		db.session.add(tag)
		db.session.commit()
	return tag

def blog_remove(blog_id):
	blog = BlogEntry.query.filter_by(id=blog_id).first()
	if blog.blog_type == 'photo':
		blog_photo = BlogEntryPhoto.query.filter_by(blog_entry_id=blog_id).first()
		if blog_photo:
			db.session.delete(blog_photo)
	
	if blog:
		db.session.delete(blog)
	db.session.commit()
