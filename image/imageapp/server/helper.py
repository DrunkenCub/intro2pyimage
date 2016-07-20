"""
"""
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

class ImageCRUD(object):
	"""
	"""

	def __init__(self):
		from ..models import Image
		from imageapp import db
		self.image = Image
		self.db = db

	def create(self, title, image_url):
		img = self.image(title=title, image_url=image_url)
		self.db.session.add(img)
		self.commit()
		return img

	def update(self):
		pass

	def read(self):
		images = self.image.query.all()
		return images

	def delete(self):
		pass

	def commit(self):
		self.db.session.commit()