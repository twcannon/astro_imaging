import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from astropy.io import fits

#### INCLUDE CONTROL HERE TO SEARCH AND ITERATE THROUGH COLORS
print 'starting Blue'
###########################################################################################################
###############################################BLUE########################################################
###########################################################################################################



#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
filepath = '../data/20170510_jupiter/250ms/blue/'

jupiter_blue_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        jupiter_blue_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'


# im = Image.merge("RGB", (jupiter_blue_image[0], jupiter_blue_image[1], jupiter_blue_image[2]))

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)

#view the numpy arrays as an images
# plt.plot(im)
# plt.colorbar()
# plt.show()


#print(done)

#test to find the dimensions of the image
#image_size = jupiter_blue_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each jupiter image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	jupiter_blue_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += jupiter_blue_image[x][i][j]
		jupiter_blue_column.append(y)
	index = np.where(jupiter_blue_column == np.max(jupiter_blue_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each jupiter image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	jupiter_blue_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += jupiter_blue_image[x][j][i]
		jupiter_blue_row.append(y)
	index = np.where(jupiter_blue_row == np.max(jupiter_blue_row))
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
jupiter_blue_vertical_shifted = []
x = 0
for x in range(loop_number):
	jupiter_blue_image[x] = np.roll(jupiter_blue_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	jupiter_blue_vertical_shifted.append(jupiter_blue_image[x])

#shift images horizontally
jupiter_blue_final_shifted = []
x = 0
for x in range(loop_number):
	jupiter_blue_vertical_shifted[x] = np.roll(jupiter_blue_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	jupiter_blue_final_shifted.append(jupiter_blue_vertical_shifted[x])

#median combine all shifted images into a final image
final_blue_image = np.median(jupiter_blue_final_shifted, axis=0)

#display final median combined numpy array
# plt.imshow(final_blue_image, cmap='Blues')
# plt.colorbar()
# plt.show()
print 'starting Red'

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
################################################RED########################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
filepath = '../data/20170510_jupiter/250ms/red/'

jupiter_red_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        jupiter_red_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)

#view the numpy arrays as an images
# x=0
# for x in range(loop_number):
	# plt.imshow(jupiter_red_image[x], cmap='Reds')
	# plt.colorbar()
	# plt.show()

#test to find the dimensions of the image
#image_size = jupiter_blue_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each jupiter image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	jupiter_red_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += jupiter_red_image[x][i][j]
		jupiter_red_column.append(y)
	index = np.where(jupiter_red_column == np.max(jupiter_red_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each jupiter image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	jupiter_red_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += jupiter_red_image[x][j][i]
		jupiter_red_row.append(y)
	index = np.where(jupiter_red_row == np.max(jupiter_red_row))
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
jupiter_red_vertical_shifted = []
x = 0
for x in range(loop_number):
	jupiter_red_image[x] = np.roll(jupiter_red_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	jupiter_red_vertical_shifted.append(jupiter_red_image[x])

#shift images horizontally
jupiter_red_final_shifted = []
x = 0
for x in range(loop_number):
	jupiter_red_vertical_shifted[x] = np.roll(jupiter_red_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	jupiter_red_final_shifted.append(jupiter_red_vertical_shifted[x])

#median combine all shifted images into a final image
final_red_image = np.median(jupiter_red_final_shifted, axis=0)

#display final median combined numpy array
# plt.imshow(final_red_image, cmap='Reds')
# plt.colorbar()
# plt.show()
print 'starting Green'

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
################################################GREEN######################################################
###########################################################################################################

#### temporarily hardcoded
#import fits files as hdulist and convert into numpy arays
filepath = '../data/20170510_jupiter/250ms/green/'

jupiter_green_image = {}
file_num = 0
for filename in os.listdir(filepath):
    if filename.endswith(".fit"): 
        print 'found image at ' + filepath + filename
        jupiter_green_image[file_num] = fits.open(filepath+filename)[0].data
        file_num+=1
    else:
    	print filename + ' is not a valid image file'

#establishing a loop that equals the number of images being used
loop_number = file_num - 1
#print(loop_number)

#view the numpy arrays as an images
# x=0
# for x in range(loop_number):
	# plt.imshow(jupiter_green_image[x], cmap='Greens')
	# plt.colorbar()
	# plt.show()

#test to find the dimensions of the image
#image_size = jupiter_blue_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each jupiter image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(loop_number):
	jupiter_green_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += jupiter_green_image[x][i][j]
		jupiter_green_column.append(y)
	index = np.where(jupiter_green_column == np.max(jupiter_green_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each jupiter image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(loop_number):
	jupiter_green_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += jupiter_green_image[x][j][i]
		jupiter_green_row.append(y)
	index = np.where(jupiter_green_row == np.max(jupiter_green_row))
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
jupiter_green_vertical_shifted = []
x = 0
for x in range(loop_number):
	jupiter_green_image[x] = np.roll(jupiter_green_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	jupiter_green_vertical_shifted.append(jupiter_green_image[x])

#shift images horizontally
jupiter_green_final_shifted = []
x = 0
for x in range(loop_number):
	jupiter_green_vertical_shifted[x] = np.roll(jupiter_green_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	jupiter_green_final_shifted.append(jupiter_green_vertical_shifted[x])

#median combine all shifted images into a final image
final_green_image = np.median(jupiter_green_final_shifted, axis=0)

#display final median combined numpy array
# plt.imshow(final_green_image, cmap='Greens')
# plt.colorbar()
# plt.show()

print 'starting RGB'

###########################################################################################################
###########################################################################################################
###########################################################################################################

###########################################################################################################
#################################################RGB#######################################################
###########################################################################################################

jupiter_rgb_image = [final_blue_image, final_red_image, final_green_image]

#Squishes each jupiter image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
x = 0
for x in range(3):
	jupiter_rgb_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += jupiter_rgb_image[x][i][j]
		jupiter_rgb_column.append(y)
	index = np.where(jupiter_rgb_column == np.max(jupiter_rgb_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each jupiter image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
x = 0
for x in range(3):
	jupiter_rgb_row = []
	for i in range(1360):
		y=0
		for j in range(1024):
			y += jupiter_rgb_image[x][j][i]
		jupiter_rgb_row.append(y)
	index = np.where(jupiter_rgb_row == np.max(jupiter_rgb_row))
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
jupiter_rgb_vertical_shifted = []
x = 0
for x in range(3):
	jupiter_rgb_image[x] = np.roll(jupiter_rgb_image[x], (indexcolumnarray[0] - indexcolumnarray[x]), axis=0)
	jupiter_rgb_vertical_shifted.append(jupiter_rgb_image[x])

#shift images horizontally
jupiter_rgb_final_shifted = []
x = 0
for x in range(3):
	jupiter_rgb_vertical_shifted[x] = np.roll(jupiter_rgb_vertical_shifted[x], (indexrowarray[0] - indexrowarray[x]), axis=1)
	jupiter_rgb_final_shifted.append(jupiter_rgb_vertical_shifted[x])

#median combine all shifted images into a final image
final_rgb_image = np.median(jupiter_rgb_final_shifted, axis=0)

arr = np.dstack([jupiter_rgb_final_shifted[0], jupiter_rgb_final_shifted[1], jupiter_rgb_final_shifted[2]])
im = Image.fromarray(arr, 'RGB')

#display final median combined numpy array
# plt.imshow(final_rgb_image, cmap='Greys')
# plt.colorbar()
# plt.show()

im.show()
###########################################################################################################
###########################################################################################################
###########################################################################################################