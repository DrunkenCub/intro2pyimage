"""
Developed for APIIT session
"""
from skimage import data, draw
from skimage import transform, util
import numpy as np
from skimage import filters, color
from matplotlib import pyplot as plt
from PIL import Image
from numpy import array

HI_COLOR = np.array([0, 1, 0])

class ObjectRemove(object):
	"""
	"""
	def __init__(self):
		self.img = None
		self.eimg = None

	def set_image(self, image_url):
		self.img = Image.open(image_url)
		self.img = array(self.img)
		self.img = util.img_as_float(self.img)
		self.eimg = filters.sobel(color.rgb2gray(self.img))

		return self.img, self.eimg

	def create_mask(self):
		masked_img = self.img.copy()

		#poly = [(2018, 2043), (2018, 2761), (2918, 2741), (2887, 2342)]
		# poly = [(41, 122), (40, 213), (108, 213), (113, 136)]
		poly = [(89, 188), (88, 263), (204, 260), (214, 188)]
		pr = np.array([p[0] for p in poly])
		pc = np.array([p[1] for p in poly])
		self.rr, self.cc = draw.polygon(pr, pc)

		masked_img[self.rr, self.cc, :] = masked_img[self.rr, self.cc, :]*0.5 + HI_COLOR*.5

	def remove_object(self):
		self.eimg[self.rr, self.cc] -= 1000
		plt.figure()
		plt.title('Object Removed')
		out = transform.seam_carve(self.img, self.eimg, 'vertical', 90)
		resized = transform.resize(self.img, out.shape)
		return out
