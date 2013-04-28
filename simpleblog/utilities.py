import datetime

from database import db
from models import *

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
	return None

#	if tag exists it is return
#	if not it will be created and returned
def create_blog_tag(title):
	tag = BlogTag.query.filter_by(title=tag).first()
	if tag == None:
		tag = BlogTag()
		storedTag.title = title
		db.session.add(tag)
		db.session.commit()
	return tag
