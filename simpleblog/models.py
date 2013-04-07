from database import db

class BlogEntry(db.Model):
	
	def __repr__(self):
		return "BlogEntry"
