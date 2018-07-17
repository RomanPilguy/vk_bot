# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 01:45:19 2018

@author: POMAH
"""
from enum import Enum
login = 'login'
password = 'pass'
token = 'token'
states_dict = {}
watermark_params = {
        
        
        }
class States(Enum):
    
    GET_PHOTOS = 'GET_PHOTOS'
    GET_WATERMARK_TYPE = 'GET_WATERMARK_TYPE'
    GET_WATERMARK_TEXT = 'GET_WATERMARK_TEXT'
    GET_WATERMARK_PHOTO = 'GET_WATERMARK_PHOTO'
    GET_WATERMARK_SIZE = 'GET_WATERMARK_SIZE'
    GET_TEXT_SIZE = 'GET_TEXT_SIZE'
    GET_TEXT_COLOR = 'GET_TEXT_COLOR'
    GET_OFFSET_X = 'GET_OFFSET_X'
    GET_OFFSET_Y = 'GET_OFFSET_Y'
    START = 'START'
    
    
watermark_types = {
        'text'  : 'Водяной знак текстом',       
        'image' : 'Водяной знак картинкой'
        
        }