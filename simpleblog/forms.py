from flask.ext.wtf import Form, TextField, TextAreaField, validators, html5, FileField

class NewTextBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])
	tags = TextField('tags')
	body = TextAreaField('Body')

class NewPhotoBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])	
	tags = TextField('tags')	
	photo_link = html5.URLField('link')
	photo_file = FileField('file')

class NewQuoteBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])
	tags = TextField('tags')
	body = TextAreaField('body')
