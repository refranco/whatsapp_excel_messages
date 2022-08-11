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
from whatsapp_automation import wp_image
sys.path.insert(1, 'C:\\Users\\Usuario\\Documents\\Python_Scripts\\proyecto_confuturo\\codigos')
import Browser

msg1 = 'camapanha_1_caption.txt'
msg2 = 'camapanha_1_caption_noname.txt'
img_path = r'C:/Users/Usuario/Documents/Python_Scripts/proyecto_confuturo/camapaña_1/campaña_1.jpeg'
init_time = datetime.time(hour = 9, minute=00, second=0)
end_time = datetime.time(hour = 17, minute=30, second=0)
contactfile = '../results/compradores_bd_Duville_2da_campanha.xlsx'
# contactfile = '../results/contact_list.xlsx'


if __name__ == '__main__':

    contact_list =  pd.read_excel(contactfile)   
    message_instant = open(msg1, encoding='utf-8').read()
    message_noname = open(msg2, encoding='utf-8').read()
    members = len(contact_list.index) # longitud lista a enviar
    i = 2  # comenzar desde este miembro
    while i < members:
        now = datetime.datetime.now().time()
        if now > init_time and now < end_time:       
            
            if i % 10 == 0 and i != 0:
                Browser.clearChromeCache() # Limpiando browser
            print(contact_list.loc[i,'Nombre'],contact_list.loc[i,'Celular'])
            if contact_list.loc[i,'Archivo Fuente'] != contact_list.loc[i,'Archivo Fuente']: 
                wp_image('+57'+str(contact_list.loc[i,'Celular']),
                        None,
                        message_noname,
                        img_path)
            else:        
                wp_image('+57'+str(contact_list.loc[i,'Celular']),
                        contact_list.loc[i,'Nombre'],
                        message_instant,
                        img_path)
            print(i, f'Actual time: {now}')
            i += 1
        else:
            print('out of office time... sleeping 1 minute')
            time.sleep(5*60)