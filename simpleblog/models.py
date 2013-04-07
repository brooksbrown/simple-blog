from database import db

class BlogEntry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))

	created = db.Column(db.DateTime)
	updated = db.Column(db.DateTime)

	def __repr__(self):
		return self.title 

class BlogEntryText(db.Model):
	blogentry_id = db.Column(db.Integer, db.ForeignKey('BlogEntry.id'))
	blogentry = db.relationship('BlogEntry',
			backref=db.backref('blogentrytext', lazy='dynamic'))

	body = db.Column(db.Text)

class BlogEntryPhoto(db.Model):
	blogentry_id = db.Column(db.Integer, db.ForeignKey('BlogEntry.id'))
	blogentry = db.relationship('BlogEntry',
			backref=db.backref('blogentrytext', lazy='dynamic'))
	
	photo_link = db.Column(db.String(180))
	photo_file = db.Column(db.String(120))

class BlogEntryQuote(db.Model):
	blogentry_id = db.Column(db.Integer, db.ForeignKey('BlogEntry.id'))
	blogentry = db.relationship('BlogEntry',
			backref=db.backref('blogentrytext', lazy='dynamic'))

	quote = db.Column(db.Text)
	source = db.Column(db.String(120))

class BlogEntryLink(db.Model):
	blogentry_id = db.Column(db.Integer, db.ForeignKey('BlogEntry.id'))
	blogentry = db.relationship('BlogEntry',
			backref=db.backref('blogentrytext', lazy='dynamic'))

	link = db.Column(db.String(180))
