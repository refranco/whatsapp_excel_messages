#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:05:06 2021

@author: esteban
"""

import pandas as pd
import pywhatkit as kit
import datetime
import time


#%%
def wp_message(phone, name):
      import pywhatkit as kit
      from datetime import datetime
      ahora = datetime.now()
      hour = ahora.hour
      minute = ahora.minute
      print(f'message will be send at {hour}:{minute+1}')
      name = name.split(' ')[0]
      try:
          kit.sendwhatmsg(phone, f'Hola {name}, Este es un mensaje automático creado desde Python', 
                          time_hour=hour, 
                          time_min=minute+1,
                          wait_time=10, 
                          tab_close=True,
                          close_time=15)
          print(f'Enviado a {name}')
      except Exception as e:
          print(e)
      
def wp_image(phone,name, caption, img_path):
    import pywhatkit as kit
    from string import Template
    if name:
        name = name.split(' ')[0]
        temp_message = Template(caption).substitute(name=name)
    else:
        temp_message = caption
    try:
        kit.sendwhats_image(receiver=phone,
                            img_path=img_path,
                            caption=temp_message,
                            wait_time=25,
                            tab_close=True,
                            close_time=5)
        
    except Exception as e:
        print(e)
        

def wp_instant(phone, name, message):
    import pywhatkit as kit
    from string import Template
    name = name.split(' ')[0]
    temp_message = Template(message).substitute(name=name)
    try:
        kit.sendwhatmsg_instantly(phone_no=phone,
                                  message=temp_message,
                                  wait_time=8,
                                  tab_close=True,close_time=1)
        print(f'mensaje enviado a {phone}')
    except Exception as e:
        print(e)
    
