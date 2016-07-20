from imageapp import db

class Image(db.Model):
	# Define the properties mapped to database columns
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False)
	image_url = db.Column(db.string(200), nullable = False)

	def __init__(self, title, image_url):
		self.title = title
		self.image_url = text

	def __repr__(self):
		return '<Image %r>' % self.title