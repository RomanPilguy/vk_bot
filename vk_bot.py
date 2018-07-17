# -*- coding: utf-8 -*-
import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
import config
import states_switcher

from vk_api import VkUpload

import start
import get_photos
import get_watermark_type
import get_watermark_text
import get_watermark_photo
import get_watermark_size

import get_offset_x
import get_offset_y

vk_session = vk_api.VkApi(token = config.token)
upload = VkUpload(vk_session)
 
vk = vk_session.get_api()


longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.START.value :
            print('id{}'.format(event.user_id))
            
            start.start(event,vk,config,states_switcher)
        
        
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_PHOTOS.value:
                
            get_photos.get_photos(event,vk,config,states_switcher)
        
        
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_WATERMARK_TYPE.value:
                
            
            get_watermark_type.get_watermark_type(event,vk,config,states_switcher)
                    
        
        
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_WATERMARK_TEXT.value:
             
            get_watermark_text.get_watermark_text(event,vk,config,states_switcher)
        
        
        
        
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_WATERMARK_PHOTO.value:         
             
            get_watermark_photo.get_watermark_photo(event,vk,config,states_switcher)
             
       
        
        
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_WATERMARK_SIZE.value:
            
            get_watermark_size.get_watermark_size(event,vk,config,states_switcher)
                    
                    
      
                
       
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_OFFSET_X.value:     
            
            get_offset_x.get_offset_x(event,vk,config,states_switcher)
          
        
        
        
        
        
        elif event.type == VkEventType.MESSAGE_NEW and event.to_me and states_switcher.get_current_state(event.user_id)  == config.States.GET_OFFSET_Y.value:
           
            get_offset_y.get_offset_y(event,vk,config,states_switcher,upload)
           
if __name__ == '__main__':
    main()