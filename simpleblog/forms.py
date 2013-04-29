from flask.ext.wtf import Form, TextField, TextAreaField, validators, html5, FileField, SubmitField

class NewTextBlogForm(Form):
	title 	= TextField('Title', [
		validators.Required()
	])
	tags 	= TextField('tags')
	body 	= TextAreaField('Body')

	draft_submit = SubmitField('Save as draft', id="draft-submit")
	post_submit = SubmitField('Post to blog', id="post-submit")

class NewPhotoBlogForm(Form):
	title 	= TextField('Title', [
		validators.Required()
	])	
	tags 	= TextField('tags')	
	link  	= html5.URLField('link')
	file 	= FileField('file')
	body 	= TextAreaField('Body')

	draft_submit = SubmitField('Save as draft', id="draft-submit")
	post_submit = SubmitField('Post to blog', id="post-submit")

class NewVideoBlogForm(Form):
	title 	= TextField('Title', [
		validators.Required()
	])
	tags 	= TextField('tags')
	link 	= TextField('link')
	body 	= TextAreaField('body')

	draft_submit = SubmitField('Save as draft', id="draft-submit")
	post_submit = SubmitField('Post to blog', id="post-submit")

class NewAudioBlogForm(Form):
	title 	= TextField('Title', [
		validators.Required()
	])
	tags 	= TextField('tags')
	link 	= TextField('link')
	body 	= TextAreaField('body')

	draft_submit = SubmitField('Save as draft', id="draft-submit")
	post_submit = SubmitField('Post to blog', id="post-submit")

class NewQuoteBlogForm(Form):
	title 	= TextField('Title', [
		validators.Required()
	])
	tags 	= TextField('tags')
	quote = TextField('quote')
	source 	= TextField('source')
	body 	= TextAreaField('body')
	
	draft_submit = SubmitField('Save as draft', id="draft-submit")
	post_submit = SubmitField('Post to blog', id="post-submit")

class NewLinkBlogForm(Form):
	title 	= TextField('Title', [
		validators.Required()
	])
	tags 	= TextField('tags')
	link 	= TextField('link')
	body 	= TextAreaField('body')
	
	draft_submit = SubmitField('Save as draft', id="draft-submit")
	post_submit = SubmitField('Post to blog', id="post-submit")


class RemoveBlogForm(Form):
	remove_submit = SubmitField('Remove')

