# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:27:41 2018

@author: POMAH
"""
import watermark_text
import watermark_photo

import os
import json
def get_offset_y(event,vk,config,states_switcher,upload):
            end = False    
            if event.text.isdigit() and end == False:
                    
                    config.watermark_params[str(event.user_id)]['offset_y'] = event.text
                    x = config.watermark_params[str(event.user_id)]['offset_x']
                    y = event.text
                    pos = (int(x),int(y))
                    attachments =[]
                    if(config.watermark_params[str(event.user_id)]['watermark_type']) == 'text':
                        text = config.watermark_params[str(event.user_id)]['text']
                        
                        for image in config.watermark_params[str(event.user_id)]['photos']:
                            watermark_text.watermark_text(input_image_path = 'assets'+chr(47) + image, 
                                                          output_image_path = 'assets\image_watermark' + str(image) +  '.png',
                                           text = text,
                                          pos = pos,
                                          size = config.watermark_params[str(event.user_id)]['watermark_size'] )
                            photo = upload.photo_messages(photos='assets\image_watermark' + str(image) +  '.png')[0]
                            os.remove('assets\image_watermark' + str(image) +  '.png')
                            os.remove('assets' + chr(47) + image)
                            attachments.append(
                                    'photo{}_{}'.format(photo['owner_id'], photo['id']))
                        
                    
                    elif config.watermark_params[str(event.user_id)]['watermark_type'] == 'photo':
                        for image in config.watermark_params[str(event.user_id)]['photos'] :
                            watermark_photo.watermark_photo(
                                    input_image_path = 'assets'+chr(47) + image, 
                                    output_image_path = 'assets\image_watermark' + str(image) +  '.png',
                                    watermark_image_path = config.watermark_params[str(event.user_id)]['watermark_photo'],
                                    position = pos,
                                    size = int(config.watermark_params[str(event.user_id)]['watermark_size'])
                                    
                                    
                                    
                                    )
                            photo = upload.photo_messages(photos='assets\image_watermark' + str(image) +  '.png')[0]
                            os.remove('assets\image_watermark' + str(image) +  '.png')
                            os.remove('assets' + chr(47) + image)
                            attachments.append(
                                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                                                )
                        os.remove(config.watermark_params[str(event.user_id)]['watermark_photo'])
                    end = True
                    
                   
            elif end == False and event.text.isdigit() == False:
                      vk.messages.send(user_id = event.user_id,message = 'Введите  целое число!')
            if end == True:
                keyboard = {
                                'one_time': True,
                                'buttons': [[{
                                'action': {
                                        'type': 'text',
                                        'payload': json.dumps({'buttons': '1'}),
                                        'label': 'Загрузить еще фотографии',
                                        },
                                        'color': 'positive'
                                        }
                                ]]}
                keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                keyboard = str(keyboard.decode('utf-8'))
                
                states_switcher.set_state(event.user_id,config.States.START.value)
             
                del config.watermark_params[str(event.user_id)]
                vk.messages.send(
                                 user_id = event.user_id,
                                 message = 'Фотографии отредактированы',
                                 attachment = ','.join(attachments),
                                 keyboard = keyboard
                                 )