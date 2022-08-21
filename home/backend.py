from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
from PIL import Image
import PIL.ImageOps
import cv2
import pandas as pd
import numpy as np
from colorthief import ColorThief
import webcolors
import os

# preprocess the image
def pprocess_image(image_path):
	im = Image.open(image_path)
	im.crop((0, 0, 5, 5))
	rgb = im.convert('RGB')# get three R G B values
	r, g, b = rgb.getpixel((1, 1))

	cwd = os.getcwd()
	file_name = os.path.basename(image_path)
	processed = os.path.join(cwd, 'processed\\', file_name)

	if(r > 200 and g > 200 and b > 200):
		img = Image.open(image_path)
		img_inverted = PIL.ImageOps.invert(img)
		img_inverted.save(processed)
		print('inverted')
	else:
		print('here')
		img = Image.open(image_path)
		img.save(processed)

	img = Image.open(processed)
	resized_img = img.resize((28, 28))
	resized_img.save("clothing2.jpg")

	#grayscaling image
	img = Image.open('clothing2.jpg')
	imgGray = img.convert('L')
	imgGray.save('clothing3.png')

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, grayscale=True, target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

# translation of index
def output_translate(output:int) -> str:
	lst_out = ['T-Shirt', 'Trouser', 'Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle Boot']
	return(lst_out[output])

# load an image and predict the class
def classify_image(image_path, mode = 0):
	cwd = os.getcwd()
	file_name = os.path.basename(image_path)
	processed = os.path.join(cwd, 'processed\\', file_name)
	# load the image
	img = load_image(processed)
	# load model
	model = load_model(r'C:\Users\derro\Documents\Code\HT6_2022\fit_chooser\home\clothing_model.h5')
	# predict the class
	
	predictions = np.where(model.predict(img) == (model.predict(img)).max())
	lst_pred = (model.predict(img)).tolist()
	
	maximum_match = (model.predict(img)).max()
	lst_possibilities = [int(predictions[1])]
	lst_pred_1 = lst_pred[0]
	if(int(predictions[1]) == 2 or int(predictions[1]) == 4):
		for i in range(len(lst_pred_1)):
			if lst_pred_1[i]/maximum_match > 0.1 and not lst_pred_1[i] == maximum_match:
				lst_possibilities.append(i)
		
	str_output = ''
	
    # prints a user-friendly response
	if mode == 0:
		# print()
		# if len(lst_possibilities) == 1:
		# 	print('Your clothing is a', output_translate(int(predictions[1])))
		# else:
		# 	print('Your clothing is a ', end = '')
		# 	for item in lst_possibilities:
		# 		str_output += output_translate(item) + ' or '
		# 	str_output = str_output.strip(' or')
		# 	print(str_output)
		return(int(predictions[1]))

    # returns list of match percentage
	elif mode == 1:
		return(output_translate(int(predictions[1])))

    # returns both list and user friendly
	elif mode == 2:
		if len(lst_possibilities) == 1:
			print('Your clothing is a', output_translate(int(predictions[1])))
		else:
			print('Your clothing is a ', end = '')
			for item in lst_possibilities:
				str_output += output_translate(item) + ' or '
			str_output = str_output.strip(' or')
			print(str_output)
		return(lst_pred_1)
        
# colour selection
def process_colour(clothing):
	BLUR = 21
	CANNY_THRESH_1 = 10
	CANNY_THRESH_2 = 200
	MASK_DILATE_ITER = 10
	MASK_ERODE_ITER = 10
	MASK_COLOR = (0.0,0.0,1.0)

	#READ IMAGE
	img = cv2.imread(clothing)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#EDGE DETECTION
	edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
	edges = cv2.dilate(edges, None)
	edges = cv2.erode(edges, None)

	#FINDING CONTOURS IN THE EDGES, SORTING BY AREA
	contour_info = []
	contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
	for c in contours:
		contour_info.append((
			c,
			cv2.isContourConvex(c),
			cv2.contourArea(c),
		))
	contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
	max_contour = contour_info[0]

	mask = np.zeros(edges.shape)
	cv2.fillConvexPoly(mask, max_contour[0], (255))

	#BLUR
	mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
	mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
	mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
	mask_stack = np.dstack([mask]*3)    

	#MASKED IMG INTO MASK_COLOR BACKGROUND
	mask_stack = mask_stack.astype('float32') / 255.0          
	img = img.astype('float32') / 255.0                                   

	#SPLIT IMAGE INTO CHANNELS
	c_red, c_green, c_blue = cv2.split(img)

	#MERGE WITH MASK FROM ONE OF PREVIOUS STEP
	img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

	#SAVE TO FILES
	cv2.imwrite("transparent.png", img_a*255)

	#GETTING COLOR (RGB)
	ct = ColorThief("transparent.png")
	dominant_coloUr = ct.get_color(quality=1)

	#NAMING COLUMN HEADERS
	index=["color", "color_name", "hex", "R", "G", "B"]
	csv = pd.read_csv(r'C:\Users\derro\Documents\Code\HT6_2022\fit_chooser\home\colors.csv', names=index, header=None)

	r = dominant_coloUr[0]
	g = dominant_coloUr[1]
	b = dominant_coloUr[2]

	#FUNCTION TO DEFINE CLOSEST COLOUR GIVEN RGB
	def closest_coloUr(rgb):
		differences = {}
		for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
			r, g, b = webcolors.hex_to_rgb(color_hex)
			differences[sum([(r - rgb[0])**2, (g - rgb[1])**2, (b - rgb[2])**2])] = color_name
		return differences[min(differences.keys())]

	#COLOUR OF CLOTHING USED IN DATABASE
	closest_colour = closest_coloUr((r,g,b))
	# print("The colour of the clothing article is:" + closest_colour)
	return (closest_colour)

def getArticle(clothing):
	pprocess_image(clothing)
	return str(classify_image(clothing))

# main
#def main(clothing):
	##process_colour(clothing)
	#pprocess_image(clothing, False)
	#print(classify_image(clothing))
	

#main("dress-white-background-design-style-evening-clothing-fabric-plaid-flowers-beautiful-long-short-repeat-concept-graphic-creation-144754376.jpg")