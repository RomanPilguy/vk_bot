# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:05:29 2018

@author: POMAH
"""

def get_watermark_type(event,vk,config,states_switcher):
    try:
        if(event.text) == config.watermark_types['text']:
                        vk.messages.send(
                                user_id = event.user_id,
                                message = 'Введите текст, который хотите поместить на фото'
                                )
                        config.watermark_params[str(event.user_id)]['watermark_type'] = 'text'
                        states_switcher.set_state(event.user_id,config.States.GET_WATERMARK_TEXT.value)
        if(event.text) == config.watermark_types['image']:
                        vk.messages.send(
                                user_id = event.user_id,
                                message = 'Отправьте изображение, которое хотите поместить на фото'
                                )
                        config.watermark_params[str(event.user_id)]['watermark_type'] = 'photo'
                        states_switcher.set_state(event.user_id,config.States.GET_WATERMARK_PHOTO.value)
    except Exception:
        print(event)
        