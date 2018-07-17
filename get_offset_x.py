# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:24:25 2018

@author: POMAH
"""

def get_offset_x(event,vk,config,states_switcher):
    try:
                if event.text.isdigit():
                    
                    config.watermark_params[str(event.user_id)]['offset_x'] = event.text
                    vk.messages.send(user_id = event.user_id,message = 'Укажите отступ по вертикали')
                    states_switcher.set_state(event.user_id,config.States.GET_OFFSET_Y.value)
                else:
                    vk.messages.send(user_id = event.user_id,message = 'Введите  целое число!')
    except Exception:
                vk.messages.send(user_id = event.user_id,message = 'Укажите отступ по горизонтали!')
    