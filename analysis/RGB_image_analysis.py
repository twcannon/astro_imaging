import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

#import cv2

#### INCLUDE CONTROL HERE TO SEARCH AND ITERATE THROUGH COLORS

#### temporarily hardcoded
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


#test to view the numpy array as an image
plt.imshow(jupiter_blue_image[2], cmap='Blues')
plt.colorbar()
plt.show()

# sys.exit('done')

#test to find the dimensions of the image
#image_size = jupiter_blue_image[0].shape
#print image_size #1024 high x 1360 wide

###########################COLUMN#####################################
#Squishes jupiter 001 pictures into column data
jupiter_blue_001_column = []
for i in range(1024):
	y=0
	for j in range(1360):
		y += jupiter_blue_image[0][i][j]
	jupiter_blue_001_column.append(y)
#print(jupiter_blue_001_column)
max_value_column_j_b_1 = (max(jupiter_blue_001_column))
print(max_value_column_j_b_1)
max_index_column_j_b_1 = jupiter_blue_001_column.index(max_value_column_j_b_1)
print(max_index_column_j_b_1)

#Squishes jupiter 015 pictures into column data
jupiter_blue_015_column = []
for i in range(1024):
	y=0
	for j in range(1360):
		y += jupiter_blue_image[14][i][j]
	jupiter_blue_015_column.append(y)
#print(jupiter_blue_015_column)
max_value_column_j_b_15 = (max(jupiter_blue_015_column))
print(max_value_column_j_b_15)
max_index_column_j_b_15 = jupiter_blue_015_column.index(max_value_column_j_b_15)
print(max_index_column_j_b_15)
######################################################################

#############################ROW######################################
#Squishes jupiter 001 pictures into row data
jupiter_blue_001_row = []
for i in range(1360):
	x=0
	for j in range(1024):
		x += jupiter_blue_image[0][j][i]
	jupiter_blue_001_row.append(x)
#print(jupiter_blue_001_row)
max_value_row_j_b_1 = (max(jupiter_blue_001_row))
print(max_value_row_j_b_1)
max_index_row_j_b_1 = jupiter_blue_001_row.index(max_value_row_j_b_1)
print(max_index_row_j_b_1)

#Squishes jupiter 015 pictures into row data
jupiter_blue_015_row = []
for i in range(1360):
	x=0
	for j in range(1024):
		x += jupiter_blue_image[14][j][i]
	jupiter_blue_015_row.append(x)
#print(jupiter_blue_015_row)
max_value_row_j_b_15 = (max(jupiter_blue_015_row))
print(max_value_row_j_b_15)
max_index_row_j_b_15 = jupiter_blue_015_row.index(max_value_row_j_b_15)
print(max_index_row_j_b_15)
######################################################################

##############################################################################################################
##############################################################################################################
##############################################################################################################
#image shift
	#axis 0 eq vertically
	#axis 1 eq horizontally
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (100), axis=1) #to the right
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (-100), axis=1) #to the left
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (100), axis=0) #down
	#jupiter_blue_015_column_shift = np.roll(jupiter_blue_image[14], (-100), axis=0) #up
#shift 1
jupiter_blue_015_vertical_shift = np.roll(jupiter_blue_image[14], (max_index_column_j_b_1 - max_index_column_j_b_15), axis=0)

plt.imshow(jupiter_blue_015_vertical_shift, cmap='Blues')
plt.colorbar()
plt.show()

#shift 2
jupiter_blue_015_final_shifted = np.roll(jupiter_blue_015_vertical_shift, (max_index_row_j_b_1 - max_index_row_j_b_15), axis=1)

plt.imshow(jupiter_blue_015_final_shifted, cmap='Blues')
plt.colorbar()
plt.show()


#stacking numpy arrays into a 3D array
image_stack_array = []
image_stack_array.append(jupiter_blue_image[0])
#image_stack_array.append(jupiter_blue_002_image)
#image_stack_array.append(jupiter_blue_003_image)
#image_stack_array.append(jupiter_blue_004_image)
#image_stack_array.append(jupiter_blue_005_image)
#image_stack_array.append(jupiter_blue_006_image)
#image_stack_array.append(jupiter_blue_007_image)
#image_stack_array.append(jupiter_blue_008_image)
#image_stack_array.append(jupiter_blue_009_image)
#image_stack_array.append(jupiter_blue_010_image)
#image_stack_array.append(jupiter_blue_011_image)
#image_stack_array.append(jupiter_blue_012_image)
#image_stack_array.append(jupiter_blue_013_image)
#image_stack_array.append(jupiter_blue_014_image)
image_stack_array.append(jupiter_blue_015_final_shifted)
#image_stack_array.append(jupiter_blue_image[14])

#median combine 3D array into one numpy array
final_image = np.median(image_stack_array, axis=0)

#display final median combined numpy array
plt.imshow(final_image, cmap='Blues')
plt.colorbar()
plt.show()

###############################testing things##################################

#Squishes into column data
array = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]])

yfinal = []
for i in range(len(array)):
	y=0
	for j in range(len(array[i])):
		y += array[i][j]
	yfinal.append(y)
print(yfinal)

#Squishes into row data
array = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]])

xfinal = []
for i in range(len(array)):
	x=0
	for j in range(len(array[i])):
		x += array[j][i]
	xfinal.append(x)
print(xfinal)