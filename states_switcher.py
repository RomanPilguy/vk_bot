# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 02:00:04 2018

@author: POMAH
"""

from config import states_dict,States

def get_current_state(user_id):
   
     try:   
        return states_dict[user_id]
     except KeyError:
            return States.START.value
     
def set_state(user_id,value):
   
        try:
            states_dict[user_id] = value
            print('switch to ' + value)
            return True
        except:
            return False