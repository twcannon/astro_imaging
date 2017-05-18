#!/usr/bin/python
import time,re

image_content = ""
while not (len(image_content)>0 and re.match("^(?!_)\w*(?<!_)$",image_content)):
	image_content = raw_input('\nWhat are you imaging? (Ex. jupiter, moon, m31...)\n'+
                'Please use only alphanumeric characters (a-z,0-9)\n')

dir_name = (time.strftime("%Y%m%d"))+'_'+image_content
