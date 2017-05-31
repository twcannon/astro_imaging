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
#print image_size #1024 x 1360

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


##############################################################################################


#attempting to allign the two images

def get_gradient(im) :
    # Calculate the x and y gradients using Sobel operator
    grad_x = cv2.Sobel(im,cv2.CV_32F,1,0,ksize=3)
    grad_y = cv2.Sobel(im,cv2.CV_32F,0,1,ksize=3)
    # Combine the two gradients
    grad = cv2.addWeighted(np.absolute(grad_x), 0.5, np.absolute(grad_y), 0.5, 0)
    return grad


if __name__ == '__main__':
    
    
    # Read 8-bit color image.
    # This is an image in which the three channels are
    # concatenated vertically.
    
    im =  cv2.imread("images/emir.jpg", cv2.IMREAD_GRAYSCALE);

    # Find the width and height of the color image
    sz = im.shape
    print sz
    height = int(sz[0] / 3);
    width = sz[1]

    # Extract the three channels from the gray scale image
    # and merge the three channels into one color image
    im_color = np.zeros((height,width,3), dtype=np.uint8 )
    for i in xrange(0,3) :
        im_color[:,:,i] = im[ i * height:(i+1) * height,:]

    # Allocate space for aligned image
    im_aligned = np.zeros((height,width,3), dtype=np.uint8 )

    # The blue and green channels will be aligned to the red channel.
    # So copy the red channel
    im_aligned[:,:,2] = im_color[:,:,2]

    # Define motion model
    warp_mode = cv2.MOTION_HOMOGRAPHY

    # Set the warp matrix to identity.
    if warp_mode == cv2.MOTION_HOMOGRAPHY :
            warp_matrix = np.eye(3, 3, dtype=np.float32)
    else :
            warp_matrix = np.eye(2, 3, dtype=np.float32)

    # Set the stopping criteria for the algorithm.
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5000,  1e-10)

    # Warp the blue and green channels to the red channel
    for i in xrange(0,2) :
        (cc, warp_matrix) = cv2.findTransformECC (get_gradient(im_color[:,:,2]), get_gradient(im_color[:,:,i]),warp_matrix, warp_mode, criteria)
    
        if warp_mode == cv2.MOTION_HOMOGRAPHY :
            # Use Perspective warp when the transformation is a Homography
            im_aligned[:,:,i] = cv2.warpPerspective (im_color[:,:,i], warp_matrix, (width,height), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
        else :
            # Use Affine warp when the transformation is not a Homography
            im_aligned[:,:,i] = cv2.warpAffine(im_color[:,:,i], warp_matrix, (width, height), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);
        print warp_matrix

    # Show final output
    cv2.imshow("Color Image", im_color)
    cv2.imshow("Aligned Image", im_aligned)
    cv2.waitKey(0)
