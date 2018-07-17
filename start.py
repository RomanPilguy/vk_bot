# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 00:56:40 2018

@author: POMAH
"""
import json
def start(event,vk,config,states_switcher):
    if event.text == 'Начать' or event.text == 'Загрузить еще фотографии' :
                vk.messages.send(user_id = event.user_id,message = 'Загрузите фотографии')
                config.watermark_params[str(event.user_id)] = {}
                states_switcher.set_state(event.user_id,config.States.GET_PHOTOS.value)
    else:
                keyboard = {
                        'one_time': True,
                        'buttons': [[{
                                'action': {
                                        'type': 'text',
                                        'payload': json.dumps({'buttons': '1'}),
                                        'label': 'Начать',
                                        },
                                        'color': 'positive'
                                        }
                                ]]}
                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                keyboard = str(keyboard.decode('utf-8'))
                vk.messages.send(
                        user_id = event.user_id,
                        message = 'Нажмите кнопку чтобы начать',
                        keyboard = keyboard
                        
                        )