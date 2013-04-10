from database import db

blog_tags = db.Table('blog_tags',
		db.Column('blog_tag_id', db.Integer, db.ForeignKey('blog_tag.id')),
		db.Column('blog_entry_id', db.Integer, db.ForeignKey('blog_entry.id'))
		)

class BlogTag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))

	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __repr__(self):
		return self.title

class BlogEntry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	
	title = db.Column(db.String(80))
	tags = db.relationship('BlogTag', secondary=blog_tags,
			backref=db.backref('text_blog_entries', lazy='dynamic'))

	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __repr__(self):
		return self.title 

class BlogEntryText(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	blog_entry_id = db.Column(db.Integer, db.ForeignKey('blog_entry.id'))
	
	body = db.Column(db.Text)


class BlogEntryPhoto(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	blog_entry_id = db.Column(db.Integer, db.ForeignKey('blog_entry.id'))
	
	photo_link = db.Column(db.String(180))
	photo_file = db.Column(db.String(120))

class BlogEntryQuote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	blog_entry_id = db.Column(db.Integer, db.ForeignKey('blog_entry.id'))
	
	quote = db.Column(db.Text)
	source = db.Column(db.String(120))

class BlogEntryLink(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	blog_entry_id = db.Column(db.Integer, db.ForeignKey('blog_entry.id'))

	link = db.Column(db.String(180))
