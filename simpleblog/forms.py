from flask.ext.wtf import Form, TextField, TextAreaField, validators

class NewTextBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])

	body = TextAreaField('Body')

class NewPhotoBlogForm(Form):
