# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
 
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos,size):
    photo = Image.open(input_image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", int(size))
    drawing.text(pos, text, fill=black, font=font)
    
    photo.save(output_image_path)