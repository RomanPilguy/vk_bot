# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:01:14 2018

@author: POMAH
"""
import requests
import json
def get_photos(event,vk,config,states_switcher):
                i = 0
                photo_arr = []
                msg = vk.messages.getById(message_ids = event.message_id, photo_sizes = 1)
                try:   
                    if msg['items'][0]['attachments']:
                        for image in msg['items'][0]['attachments']:
                            if image['type'] == 'photo':
                            
                            
                                photo_url = image['photo']['sizes'][len(image['photo']['sizes']) - 1]['src']
                                
                                source_photo =   'photo' + str(image['photo']['id']) + '_' + str(event.user_id) +  '.png'
                                photo_arr.append(source_photo)
                                
                                response = requests.get(photo_url, stream = True)
                                
                                
                                
                                print(i)
                                if response.status_code == 200:
                                    with open('assets\photo' + str(image['photo']['id']) + '_' + str(event.user_id) +   '.png', 'wb') as f:
                                        f.write(response.content)
                                
                                
                                
                                del response
                                i+=1
                except Exception:
                    i = 0
                    
                
                
                if i > 0:
                    config.watermark_params[str(event.user_id)]['photos'] = photo_arr
                    vk.messages.send(
                            user_id = event.user_id,
                            message = 'Вы прислали ' + str(i) + ' фото')
                    keyboard = {
                        'one_time': True,
                        'buttons': [[{
                                'action': {
                                        'type': 'text',
                                        'payload': json.dumps({'buttons': '1'}),
                                        'label': config.watermark_types['image'],
                                        },
                                        'color': 'negative'
                                        },
                                        {
                                                'action': {
                                                        'type': 'text',
                                                        'payload': json.dumps({'buttons': '2'}),
                                                        'label': config.watermark_types['text'],
                                                        },
                                                        'color': 'primary'
                                        }
                                    ]]
                            }
                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                    keyboard = str(keyboard.decode('utf-8'))
                    vk.messages.send(
                        user_id = event.user_id,
                        message = 'Какой водяной знак вы хотите?',
                        keyboard = keyboard
                        
                        )
                   
                    states_switcher.set_state(event.user_id,config.States.GET_WATERMARK_TYPE.value)
                    
                           
                        
                else:
                    
                    
            
                    vk.messages.send(
                        user_id = event.user_id,
                        message = 'Вы не прислали ни одной фотографии',
                        )   