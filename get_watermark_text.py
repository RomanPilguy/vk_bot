# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:11:23 2018

@author: POMAH
"""

def get_watermark_text(event,vk,config,states_switcher):
    try:
                    config.watermark_params[str(event.user_id)]['text'] = event.text
                    vk.messages.send(user_id = event.user_id,message = 'Укажите размер текста')
                    states_switcher.set_state(event.user_id,config.States.GET_WATERMARK_SIZE.value)
    except Exception:
                    vk.messages.send(
                            user_id = event.user_id,
                            message = 'Введите текст!'
                            )