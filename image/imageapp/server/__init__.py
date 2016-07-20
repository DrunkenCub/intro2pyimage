from flask import Blueprint
from flask import redirect, request
from flask import Flask, render_template, request
from werkzeug import secure_filename
from helper import ImageCRUD
import os
from flask import jsonify, session
from ..object_remove import ObjectRemove
from matplotlib import pyplot as plt
import random


bp = Blueprint('server', __name__)

@bp.route('/upload', methods=['POST', 'GET'])
def upload():
	try:
		if request.method == 'POST':
			f = request.files['file']
			filename = secure_filename(f.filename)
			f.save(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "uploads", filename))
			image = _saveFiles(f.filename)
			session['filename'] = image.title
			session['filepath'] = image.image_url
			return render_template('index.html', image=image)
	except Exception as e:
		raise e

	return render_template('index.html', image=None)

@bp.route('/uploader')
def uploader():
	return render_template('upload.html')

@bp.route('/list')
def list():
	image_crud = ImageCRUD()
	images = image_crud.read()
	return render_template('list.html', images=images)

@bp.route('/object_remove', methods=['POST','GET'])
def object_remove():
	image = None
	if request.method == 'POST':
		obj = ObjectRemove()
		print session['filepath']
		print session['filepath']
		obj.set_image(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static") + "/" + str(session['filepath']))
		obj.create_mask()
		new_image = obj.remove_object()
		result_image_name = "result" + str(random.randint(0,10000)) + ".jpg" 
		plt.imsave(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "uploads", result_image_name) , new_image)
		image = _saveFiles(result_image_name)

	return render_template('index.html', image=image)

def _saveFiles(filename):
	image_crud = ImageCRUD()
	return image_crud.create(title=filename, 
		image_url= "uploads" + "/" + filename)


