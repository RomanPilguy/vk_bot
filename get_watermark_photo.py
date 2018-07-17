# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:14:44 2018

@author: POMAH
"""
import requests
def get_watermark_photo(event,vk,config,states_switcher):
        msg = vk.messages.getById(message_ids = event.message_id, photo_sizes = 1)    
        try:
                 get_photo = False
                 for item in msg['items'][0]['attachments']:
                     if item['type'] == 'photo' :
                         photo_url = item['photo']['sizes'][len(item['photo']['sizes']) - 1]['src']
                         photo_path =   'assests\watermark_photo' + str(item['photo']['id']) + '_' + str(event.user_id) +   '.png'               
                         response = requests.get(photo_url, stream = True)
                                
                         if response.status_code == 200:
                                    with open(photo_path, 'wb') as f:
                                        f.write(response.content)
                         config.watermark_params[str(event.user_id)]['watermark_photo'] = photo_path
                         del response
                         get_photo = True
                         break;     
                                
                                
                         
                      
                     elif item['type'] == 'doc' and item['doc']['type'] == 4:
                         photo_url = item['doc']['url']
                         photo_path  =   'assets\watermark_photo' + str(item['doc']['id']) + '_' + str(event.user_id) +   '.png'               
                         response = requests.get(photo_url, stream = True)
                                
                         if response.status_code == 200:
                                    with open(photo_path , 'wb') as f:
                                        f.write(response.content)
                          
                                
                                
                         del response
                         get_photo = True
                         config.watermark_params[str(event.user_id)]['watermark_photo'] = photo_path 
                         
                     else :
                        vk.messages.send(user_id = event.user_id,message = 'Отправьте картинку!')
                 
                 if get_photo:
                     states_switcher.set_state(event.user_id,config.States.GET_WATERMARK_SIZE.value)
                     vk.messages.send(user_id = event.user_id,message = 'Укажите размер водяного знака')
        except Exception:
                 vk.messages.send(user_id = event.user_id,message = 'Отправьте картинку!')