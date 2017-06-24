import os,sys,re
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from PIL import Image
import pylab as py


FILEPATH = '../data/'

print 'Which data would you like to process?'
observation_filepaths = {}
obs_count = 1
objects = [name for name in os.listdir(FILEPATH) if os.path.isdir(os.path.join(FILEPATH, name))]
for obs in objects:
	exposures = [name for name in os.listdir(FILEPATH+obs) if os.path.isdir(os.path.join(FILEPATH+obs, name))]
	for exp in exposures:
		print str(obs_count)+' - '+str(obs)+' at an exposure of '+str(exp)
		observation_filepaths[obs_count] = '../data/'+str(obs)+'/'+str(exp)
		obs_count+=1

obs_number = ""
while not (len(obs_number)>0 and re.match("^(?!_)\w*(?<!_)$",obs_number)):
    obs_number = raw_input('Select a Number above (Ex. 1,2,3,...)\n'+
                'Please use only numeric characters (0-9)\n')
all_filt_paths = [name for name in os.listdir(observation_filepaths[int(obs_number)]) if os.path.isdir(os.path.join(observation_filepaths[int(obs_number)], name))]

for filt_path in all_filt_paths:
	if any(file.endswith(".fit") for file in os.listdir(observation_filepaths[int(obs_number)]+'/'+filt_path)):
		filepath = observation_filepaths[int(obs_number)]+'/'+filt_path+'/'

		filt = {}
		file_num = 0
		for filename in os.listdir(filepath):
		    if filename.endswith(".fit"): 
		        filt[file_num] = fits.open(filepath+filename)[0].data
		        file_num+=1
		    else:
		    	next

		loop_number = file_num - 1
		#stack dark image numpy arrays 
		filt_stack = []
		for x in range(0,loop_number):
			filt_stack.append(filt[x])

		#median combine all dark images into a final image
		final_darks = np.median(filt_stack, axis=0)

		sys.exit('done')

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
################################################RED########################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
#filepath = '../data/20170613_venus/3ms/red/'
#filepath = '../data/20170613_saturn/19ms/red/'
filepath = '../data/20170510_jupiter/100ms/red/'
#filepath = '../data/20170510_jupiter/250ms/red/'

red_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        red_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)

#subtract darks from numpy arrays and view images
x=0
for x in range(0,loop_number):
	red_image[x] = (red_image[x] - final_darks)
	img = Image.fromarray(red_image[x], 'RGB')
	plt.imshow(red_image[x], cmap='Reds')
	plt.colorbar()
	plt.show()

#test to find the dimensions of the image
#image_size = red_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	red_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += red_image[x][i][j]
		red_column.append(y)
	index = np.where(red_column == np.max(red_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	red_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += red_image[x][j][i]
		red_row.append(y)
	index = np.where(red_row == np.max(red_row))
	indexrowarray.append(index[0][0])
print(indexrowarray)
#print(indexrowarray[0])

#shift images vertically
red_vertical_shifted = []
x = 0
for x in range(loop_number):
	red_image[x] = np.roll(red_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	red_vertical_shifted.append(red_image[x])

#shift images horizontally
red_final_shifted = []
x = 0
for x in range(loop_number):
	red_vertical_shifted[x] = np.roll(red_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	red_final_shifted.append(red_vertical_shifted[x])

#median combine all shifted images into a final image
final_red_image = np.median(red_final_shifted, axis=0)

#display final median combined numpy array
plt.imshow(final_red_image, cmap='Reds')
plt.colorbar()
plt.show()

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
################################################GREEN######################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
#filepath = '../data/20170613_venus/3ms/green/'
#filepath = '../data/20170613_saturn/19ms/green/'
filepath = '../data/20170510_jupiter/100ms/green/'
#filepath = '../data/20170510_jupiter/250ms/green/'

green_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        green_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)


#subtract darks from numpy arrays and view images
x=0
for x in range(loop_number):
	green_image[x] = (green_image[x] - final_darks)
	plt.imshow(green_image[x], cmap='Greens')
	plt.colorbar()
	plt.show()

#test to find the dimensions of the image
#image_size = green_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	green_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += green_image[x][i][j]
		green_column.append(y)
	index = np.where(green_column == np.max(green_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	green_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += green_image[x][j][i]
		green_row.append(y)
	index = np.where(green_row == np.max(green_row))
	indexrowarray.append(index[0][0])
print(indexrowarray)
#print(indexrowarray[0])

#shift images vertically
green_vertical_shifted = []
x = 0
for x in range(loop_number):
	green_image[x] = np.roll(green_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	green_vertical_shifted.append(green_image[x])

#shift images horizontally
green_final_shifted = []
x = 0
for x in range(loop_number):
	green_vertical_shifted[x] = np.roll(green_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	green_final_shifted.append(green_vertical_shifted[x])

#median combine all shifted images into a final image
final_green_image = np.median(green_final_shifted, axis=0)

#display final median combined numpy array
plt.imshow(final_green_image, cmap='Greens')
plt.colorbar()
plt.show()

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
###############################################BLUE########################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
#filepath = '../data/20170613_venus/3ms/blue/'
#filepath = '../data/20170613_saturn/19ms/blue/'
filepath = '../data/20170510_jupiter/100ms/blue/'
#filepath = '../data/20170510_jupiter/250ms/blue/'

blue_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        blue_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)


#subtract darks from numpy arrays and view images
x=0
for x in range(loop_number):
	blue_image[x] = (blue_image[x] - final_darks)
	plt.imshow(blue_image[x], cmap='Blues')
	plt.colorbar()
	plt.show()
#only use if using skimage.io
#	io.imshow(jupiter_blue_image[x])
#	io.show()

#test to find the dimensions of the image
#image_size = blue_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	blue_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += blue_image[x][i][j]
		blue_column.append(y)
	index = np.where(blue_column == np.max(blue_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	blue_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += blue_image[x][j][i]
		blue_row.append(y)
	index = np.where(blue_row == np.max(blue_row))
	indexrowarray.append(index[0][0])
print(indexrowarray)
#print(indexrowarray[0])

#image shift key
	#axis 0 eq vertically
	#axis 1 eq horizontally
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (100), axis=1) #to the right
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (-100), axis=1) #to the left
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (100), axis=0) #down
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (-100), axis=0) #up

#shift images vertically
blue_vertical_shifted = []
x = 0
for x in range(loop_number):
	blue_image[x] = np.roll(blue_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	blue_vertical_shifted.append(blue_image[x])

#shift images horizontally
blue_final_shifted = []
x = 0
for x in range(loop_number):
	blue_vertical_shifted[x] = np.roll(blue_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	blue_final_shifted.append(blue_vertical_shifted[x])

#median combine all shifted images into a final image
final_blue_image = np.median(blue_final_shifted, axis=0)

#display final median combined numpy array
plt.imshow(final_blue_image, cmap='Blues')
plt.colorbar()
plt.show()

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
#################################################RGB#######################################################
###########################################################################################################

rgb_image = [final_red_image, final_green_image, final_blue_image]

#Squishes each jupiter image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(3):
	rgb_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += rgb_image[x][i][j]
		rgb_column.append(y)
	index = np.where(rgb_column == np.max(rgb_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each jupiter image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(3):
	rgb_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += rgb_image[x][j][i]
		rgb_row.append(y)
	index = np.where(rgb_row == np.max(rgb_row))
	indexrowarray.append(index[0][0])
print(indexrowarray)
#print(indexrowarray[0])

#shift images vertically
rgb_vertical_shifted = []
x = 0
for x in range(3):
	rgb_image[x] = np.roll(rgb_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	rgb_vertical_shifted.append(rgb_image[x])

#shift images horizontally
rgb_final_shifted = []
x = 0
for x in range(3):
	rgb_vertical_shifted[x] = np.roll(rgb_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	rgb_final_shifted.append(rgb_vertical_shifted[x])

#############################################################
##blocks out jupiter so you can see the moons
##only valid for this particular image set
#for i in range(1360):
#	y=0
#	for j in range(1024):
#		y = rgb_final_shifted[0][j][i]
#		if y > 5000.0:
#			y = 2000.0
#		rgb_final_shifted[0][j][i] = y
#
#for i in range(1360):
#	y=0
#	for j in range(1024):
#		y = rgb_final_shifted[1][j][i]
#		if y > 5000.0:
#			y = 2000.0
#		rgb_final_shifted[1][j][i] = y
#
#for i in range(1360):
#	y=0
#	for j in range(1024):
#		y = rgb_final_shifted[2][j][i]
#		if y > 5000.0:
#			y = 2000.0
#		rgb_final_shifted[2][j][i] = y
#
#rgb_final_shifted[0] = (rgb_final_shifted[0]/(5000))
#rgb_final_shifted[1] = (rgb_final_shifted[1]/(5000))
#rgb_final_shifted[2] = (rgb_final_shifted[2]/(5000))
#############################################################

#creating and displaying a proper rgb image
rgb_final_shifted[0] = (rgb_final_shifted[0]/(65536))
rgb_final_shifted[1] = (rgb_final_shifted[1]/(65536))
rgb_final_shifted[2] = (rgb_final_shifted[2]/(65536))

rgbArray = np.zeros((1024,1360,3))
rgbArray[..., 0] = rgb_final_shifted[0]
rgbArray[..., 1] = rgb_final_shifted[1]
rgbArray[..., 2] = rgb_final_shifted[2]
py.clf
py.imshow(rgbArray, aspect='equal')
py.title('Final RGB Image')
py.savefig('jupiter_image.png')

#creating and display an improperly final combined numpy array as an image (just so you can see how it looks)
final_rgb_image = ((rgb_final_shifted[0]*0.3)+(rgb_final_shifted[1]*0.3)+(rgb_final_shifted[2]*0.3))

plt.imshow(final_rgb_image, cmap='Greys')
plt.colorbar()
plt.show()

plt.imshow(final_rgb_image)
plt.colorbar()
plt.show()

###########################################################################################################
###########################################################################################################
###########################################################################################################