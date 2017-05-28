from astropy.io import fits
import matplotlib.pyplot as plt


jupiter_blue_001 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_001.fit')
jupiter_blue_002 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_002.fit')
jupiter_blue_003 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_003.fit')
jupiter_blue_004 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_004.fit')
jupiter_blue_005 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_005.fit')
jupiter_blue_006 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_006.fit')
jupiter_blue_007 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_007.fit')
jupiter_blue_008 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_008.fit')
jupiter_blue_009 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_009.fit')
jupiter_blue_010 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_010.fit')
jupiter_blue_011 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_011.fit')
jupiter_blue_012 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_012.fit')
jupiter_blue_013 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_013.fit')
jupiter_blue_014 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_014.fit')
jupiter_blue_015 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p25Seconds/JupiterB_015.fit')

jupiter_blue_001_image = jupiter_blue_001[0].data
plt.imshow(jupiter_blue_001_image, cmap='Blues')
plt.colorbar()
plt.show()

#jupiter_moons_blue_001 = fits.open('/Users/lesagesj/PycharmProjects/astro_imaging/analysis/Observing_5_10_2017/Jupiter/p1Second/JupiterB_001.fit')
#jupiter_moons_blue_001_image = jupiter_moons_blue_001[0].data
#plt.imshow(jupiter_moons_blue_001_image, cmap='Blues')
#plt.colorbar()
#plt.show()