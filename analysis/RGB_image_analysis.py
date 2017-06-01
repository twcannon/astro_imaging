from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
#import cv2

#import fits files as hdulist
jupiter_blue_001 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_001.fit')
jupiter_blue_002 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_002.fit')
jupiter_blue_003 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_003.fit')
jupiter_blue_004 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_004.fit')
jupiter_blue_005 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_005.fit')
jupiter_blue_006 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_006.fit')
jupiter_blue_007 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_007.fit')
jupiter_blue_008 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_008.fit')
jupiter_blue_009 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_009.fit')
jupiter_blue_010 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_010.fit')
jupiter_blue_011 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_011.fit')
jupiter_blue_012 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_012.fit')
jupiter_blue_013 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_013.fit')
jupiter_blue_014 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_014.fit')
jupiter_blue_015 = fits.open('Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_015.fit')


#converting hdulist into numpy arrays
jupiter_blue_001_image = jupiter_blue_001[0].data
jupiter_blue_002_image = jupiter_blue_002[0].data
jupiter_blue_003_image = jupiter_blue_003[0].data
jupiter_blue_004_image = jupiter_blue_004[0].data
jupiter_blue_005_image = jupiter_blue_005[0].data
jupiter_blue_006_image = jupiter_blue_006[0].data
jupiter_blue_007_image = jupiter_blue_007[0].data
jupiter_blue_008_image = jupiter_blue_008[0].data
jupiter_blue_009_image = jupiter_blue_009[0].data
jupiter_blue_010_image = jupiter_blue_010[0].data
jupiter_blue_011_image = jupiter_blue_011[0].data
jupiter_blue_012_image = jupiter_blue_012[0].data
jupiter_blue_013_image = jupiter_blue_013[0].data
jupiter_blue_014_image = jupiter_blue_014[0].data
jupiter_blue_015_image = jupiter_blue_015[0].data

#test to view the numpy array as an image
plt.imshow(jupiter_blue_001_image, cmap='Blues')
plt.colorbar()
plt.show()

plt.imshow(jupiter_blue_015_image, cmap='Blues')
plt.colorbar()
plt.show()

#test to find the dimensions of the image
#image_size = jupiter_blue_001_image.shape
#print image_size #1024 high x 1360 wide

#stacking numpy arrays into a 3D array
image_stack_array = []
image_stack_array.append(jupiter_blue_001_image)
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
image_stack_array.append(jupiter_blue_015_image)

#median combine 3D array into one numpy array
final_image = np.median(image_stack_array, axis=0)

#display final median combined numpy array
plt.imshow(final_image, cmap='gray')
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