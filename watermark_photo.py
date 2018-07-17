# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:31:29 2018

@author: POMAH
"""
from PIL import Image
 
def watermark_photo(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position,size):
    base_image = Image.open(input_image_path).convert('RGBA')
    watermark = Image.open(watermark_image_path).convert('RGBA')
    
    width, height = base_image.size
 
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    resized_wmark = watermark.resize((int(width/100 * size),int(height/100 * size)), Image.ANTIALIAS).convert('RGBA')
    transparent.paste(resized_wmark,
                                            position, 
                                            mask=resized_wmark)
    
    transparent.save(output_image_path)

   
   