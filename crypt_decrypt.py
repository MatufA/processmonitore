# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:57:52 2018

@author: adiel
"""
#from cryptography.fernet import Fernet
from Crypto.Cipher import XOR
import base64
import string
import random

'''
def crypto (line_to_crypto, key):
    cipher_suite = Fernet(key)
    line_to_crypto = line_to_crypto.encode('utf-8')
    cipher_text = cipher_suite.encrypt(line_to_crypto)
    return cipher_text

def decrypt(line_to_decrypt, key):
    cipher_suite = Fernet(key)
    line_to_decrypt = line_to_decrypt.encode('utf-8')
    plain_text = cipher_suite.decrypt(line_to_decrypt)
    return plain_text
'''
def crypt_list(proc_list, key):
    cipher_list = []
    cipher = XOR.new(key)
    for plaintext in proc_list[:-3]:
        cipher_list.append(base64.b64encode(cipher.encrypt(plaintext)))
    cipher_list.append(proc_list[-2])
    cipher_list.append(proc_list[-1])
    return cipher_list
    
def decrypt_list(proc_list, key):
    plain_list = []
    cipher = XOR.new(key)
    for ciphertext in proc_list[:-3]:
        if ciphertext: plain_list.append(cipher.decrypt(base64.b64decode(ciphertext)))
    return plain_list

def generate_key():
    characters = string.ascii_letters  + string.digits
    password =  "".join(random.choice(characters) for x in range(random.randint(16,32)))
    return password