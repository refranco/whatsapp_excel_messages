#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:13:39 2022

@author: esteban
"""
import pandas as pd
import pywhatkit as kit
import datetime
import time
import sys
from whatsapp_automation import wp_image, wp_instant
# import Browser
import os

cwd = os.getcwd()

msg1 = f'{cwd}/../msg1.txt'
# msg2 = f'{cwd}/../msg2.txt'
# msg3 = f'{cwd}/../msg3.txt'
contactfile = f'{cwd}/../ejemplo.xlsx'
init_time = datetime.time(hour = 0, minute=00, second=0)
end_time = datetime.time(hour = 20, minute=30, second=0)

if __name__ == '__main__':

    contact_list =  pd.read_excel(contactfile)   
    message1 = open(msg1, encoding='utf-8').read()
    # message2 = open(msg2, encoding='utf-8').read()
    # message3 = open(msg3, encoding='utf-8').read()
    
    members = len(contact_list.index) # longitud lista a enviar
    i = 0 # comenzar desde este miembro
    while i < members:
        now = datetime.datetime.now().time()
        
        nombre = contact_list.loc[i,'Nombre']
        celular = '+'+str(contact_list.loc[i,'Celular'])
        if now > init_time and now < end_time:       
            
            # if i % 10 == 0 and i != 0:
            #     Browser.clearChromeCache() # Limpiando browser
            
            print(i,nombre,celular)
            # Envio mensaje de saludo personal.
            wp_instant(celular, nombre, message1)
            # Envio segundo mensaje.
            # kit.sendwhatmsg_instantly(celular,message2, wait_time=10,
            #                           tab_close=True, close_time=2)
            # # Envio tercer mensaje.
            # kit.sendwhatmsg_instantly(celular,message3, wait_time=10,
            #                           tab_close=True, close_time=2)
            
            i += 1
        else:
            print('out of office time... sleeping 1 minute')
            time.sleep(5*60)