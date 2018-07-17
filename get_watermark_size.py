# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:18:35 2018

@author: POMAH
"""

def get_watermark_size(event,vk,config,states_switcher):
    try:
                if event.text.isdigit():
                    
                    config.watermark_params[str(event.user_id)]['watermark_size'] = event.text
                    vk.messages.send(user_id = event.user_id,message = 'Укажите отступ по горизонтали')
                    states_switcher.set_state(event.user_id,config.States.GET_OFFSET_X.value)
                else:
                    vk.messages.send(user_id = event.user_id,message = 'Размер картинки - целое число!')
    except Exception:
                    vk.messages.send(user_id = event.user_id,message = 'Укажите размер водяного знака!')