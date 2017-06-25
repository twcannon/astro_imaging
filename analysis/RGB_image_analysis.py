import os,sys,re
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from PIL import Image
import pylab as py
from terminalUtils import progress
import glob



def process_switch(filepaths):
	if all (filts in filepaths for filts in ('darks','red','blue','green')):
		return RGB_switch(filepaths)



def RGB_switch(filepaths):
	final_darks = dark(filepaths['darks'],'darks',"Greys_r")
	red_image = color(filepaths['red'],'red',"Reds_r",final_darks),
	green_image = color(filepaths['green'],'green',"Greens_r",final_darks),
	blue_image = color(filepaths['blue'],'blue',"Blues_r",final_darks)
	return [red_image,green_image,blue_image]



def color(filt_filepath,filt,colormap,final_darks):
	fit_image = {}
	file_num = 0
	file_total = len(glob.glob1(filt_filepath,"*.fit"))

	for filename in os.listdir(filt_filepath):
	    if filename.endswith(".fit"): 
	        fit_image[file_num] = fits.open(filt_filepath+filename)[0].data
	        progress(file_num+1, file_total, status=('loading '+filt+' files'))
	        file_num+=1
	    else:
	    	print filename + ' is not a valid image file, Skipping...'

	print '' # this is a hack that was needed to get the progress bar to work?????
	print 'Processing '+str(file_total)+' files...'	

	#subtract darks from numpy arrays and view images
	loop_number = file_num - 1
	for x in range(0,loop_number):
		fit_image[x] = (fit_image[x] - final_darks)

	image_size = fit_image[0].shape # find the dimensions of the image

	#Squishes each image into a 1D column array and finds where the max value is (vertical)
	print 'Centering '+filt+' images vertically'
	indexcolumnarray = []
	for x in range(0,loop_number):
		fit_column = []
		for i in range(image_size[0]):
			y=0
			for j in range(image_size[1]):
				y += fit_image[x][i][j]
			fit_column.append(y)
		index = np.where(fit_column == np.max(fit_column))
		indexcolumnarray.append(index[0][0])
	
	#Squishes each image into a 1D row array and finds where the max value is (horizontal)
	print 'Centering '+filt+' images horizontally'
	indexrowarray = []
	for x in range(0,loop_number):
		fit_row = []
		for i in range(image_size[1]):
			y=0
			for j in range(image_size[0]):
				y += fit_image[x][j][i]
			fit_row.append(y)
		index = np.where(fit_row == np.max(fit_row))
		indexrowarray.append(index[0][0])

	#shift images vertically
	fit_vertical_shifted = []
	for x in range(0,loop_number):
		fit_image[x] = np.roll(fit_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
		fit_vertical_shifted.append(fit_image[x])

	#shift images horizontally
	green_final_shifted = []
	for x in range(0,loop_number):
		fit_vertical_shifted[x] = np.roll(fit_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
		green_final_shifted.append(fit_vertical_shifted[x])

	print 'Combining centered images'
	final_fit_image = np.median(green_final_shifted, axis=0)

	# optional plotting. comment out if not wanted.
	plt.imshow(final_fit_image, cmap=colormap)
	plt.colorbar()
	plt.show()

	return final_fit_image



def dark(filt_filepath,filt,colormap):

	fit_image = {}
	file_num = 0
	file_total = len(glob.glob1(filt_filepath,"*.fit"))

	for filename in os.listdir(filt_filepath):
	    if filename.endswith(".fit"): 
	        fit_image[file_num] = fits.open(filt_filepath+filename)[0].data
	        progress(file_num+1, file_total, status=('loading '+filt+' files'))
	        file_num+=1
	    else:
	    	print filename + ' is not a valid image file, Skipping...'

	loop_number = file_num - 1
	#stack dark image numpy arrays 
	filt_stack = []
	for x in range(0,loop_number):
		filt_stack.append(fit_image[x])

	print '' # this is a hack that was needed to get the progress bar to work?????
	print 'Combining dark images'
	final_darks = np.median(filt_stack, axis=0)

	# optional plotting. comment out if not wanted.
	# plt.imshow(final_darks, cmap=colormap)
	# plt.colorbar()
	# plt.show()

	return final_darks




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

filepaths = {}
for filt in all_filt_paths:
	if len(glob.glob1(observation_filepaths[int(obs_number)]+'/'+filt,"*.fit")) > 0:
		print 'Adding '+filt+' to filepath list'
		filepaths[filt] = observation_filepaths[int(obs_number)]+'/'+filt+'/'
	else:
		print 'No fits files exist in '+observation_filepaths[int(obs_number)]+'/'+filt+'. Skipping...'
rgb_image = process_switch(filepaths)
print rgb_image
print 'red'
print rgb_image[0]
print 'green'
print rgb_image[1]
print 'blue'
print rgb_image[2]

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