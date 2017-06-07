import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

#### INCLUDE CONTROL HERE TO SEARCH AND ITERATE THROUGH COLORS

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


#view the numpy arrays as an images
f=0
for f in range(0,14):
	plt.imshow(jupiter_blue_image[f], cmap='Blues')
	plt.colorbar()
	plt.show()

# sys.exit('done')

#test to find the dimensions of the image
#image_size = jupiter_blue_image[0].shape
#print image_size #1024 high x 1360 wide

#Squishes each jupiter image into a 1D column array and finds where the max value is (vertical)
indexcolumnarray = []
loop_num = 0
for loop_num in range(0,14):
	jupiter_blue_column = []
	for i in range(1024):
		y=0
		for j in range(1360):
			y += jupiter_blue_image[loop_num][i][j]
		jupiter_blue_column.append(y)
	index = np.where(jupiter_blue_column == np.max(jupiter_blue_column))
	indexcolumnarray.append(index[0][0])
print(indexcolumnarray)
#print(indexcolumnarray[0])

#Squishes each jupiter image into a 1D row array and finds where the max value is (horizontal)
indexrowarray = []
loop_number = 0
for loop_number in range(0,14):
	jupiter_blue_row = []
	for i in range(1360):
		x=0
		for j in range(1024):
			x += jupiter_blue_image[loop_number][j][i]
		jupiter_blue_row.append(x)
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
loop_numb = 0
for loop_numb in range(0,14):
	jupiter_blue_image[loop_numb] = np.roll(jupiter_blue_image[loop_numb], (indexcolumnarray[0] - indexcolumnarray[loop_numb]), axis=0)
	jupiter_blue_vertical_shifted.append(jupiter_blue_image[loop_numb])

#shift images horizontally
jupiter_blue_final_shifted = []
loop_numero = 0
for loop_numero in range(0,14):
	jupiter_blue_vertical_shifted[loop_numero] = np.roll(jupiter_blue_vertical_shifted[loop_numero], (indexrowarray[0] - indexrowarray[loop_numero]), axis=1)
	jupiter_blue_final_shifted.append(jupiter_blue_vertical_shifted[loop_numero])

#median combine all shifted images into a final image
final_image = np.median(jupiter_blue_final_shifted, axis=0)

#display final median combined numpy array
plt.imshow(final_image, cmap='Blues')
plt.colorbar()
plt.show()