#images in a directory to PDF
#Uses img2pdf package


import os
import img2pdf

dirname = ''

with open("pdf","wb") as f:
	imgs = []
	for name in os.listdir(dirname):
		if not name.endswith(".png"):
			continue
		path = os.path.join(dirname, name)
		if os.path.isdir(path):
			continue
		imgs.append(path)
	f.write(img2pdf.convert(imgs))
