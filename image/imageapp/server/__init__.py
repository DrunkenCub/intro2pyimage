from flask import Blueprint
from flask import redirect, request
from flask import Flask, render_template, request
from werkzeug import secure_filename
from helper import ImageCRUD
import os
from flask import jsonify
from ..object_remove import ObjectRemove
from matplotlib import pyplot as plt


bp = Blueprint('server', __name__)

@bp.route('/upload', methods=['POST', 'GET'])
def upload():
	try:
		if request.method == 'POST':
			f = request.files['file']
			f.save(secure_filename(f.filename))
			_saveFiles(f)
			return 'file uploaded successfully'
	except Exception as e:
		raise e

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
		file = request.form.get('file_name', None)
		print file
		obj = ObjectRemove()
		obj.set_image(file)
		obj.create_mask()
		new_image = obj.remove_object()
		plt.imsave("3new.jpg" , new_image)
		image = _saveFiles(file)
	return render_template('show.html', image=image)

def _saveFiles(file):
	image_crud = ImageCRUD()
	return image_crud.create(title=file, 
		image_url= os.path.abspath(
			os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/" + "3new.jpg")


