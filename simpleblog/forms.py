from flask.ext.wtf import Form, TextField, TextAreaField, validators

class NewTextBlogForm(Form):
	title = TextField('Title', [
		validators.Required()
	])
	tag1 = TextField('tag1')
	body = TextAreaField('Body')

