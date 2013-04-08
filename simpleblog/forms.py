from flask.ext.wtf import Form, TextField, TextAreaField, validators, html5, FileField

class NewTextBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])

	body = TextAreaField('Body')

class NewPhotoBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])

	photo_link = html5.URLField('link')

	photo_file = FileField('file')

class NewQuoteBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])

	body = TextAreaField('Body')
	source = TextField('Source')

