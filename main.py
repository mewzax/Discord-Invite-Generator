import random
import time
import httpx
import string
import itertools
import json

__CONFIG__ = json.load(open('./config.json'))
__PROXIES__ = itertools.cycle(open(__CONFIG__['path_proxies'], 'r+').read().splitlines())

print(
    '''
    
██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗  ░██████╗░███████╗███╗░░██╗
██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝  ██╔════╝░██╔════╝████╗░██║
██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗  ╚██████╔╝███████╗██║░╚███║
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝'''
)
print('Made by Mewzax')

saveValidCodes = input('Do you want to save valid codes? (y/n) ')
saveInvalidCodes = input('Do you want to save invalid codes? (y/n) ')

chars = []
chars[:0] = string.ascii_letters + string.digits

def saveCodes(code, file):
    with open(file, 'a') as f:
        f.write('\n' + code)

def checkCode(code):
    try:
        with httpx.Client(proxies= f'http://{next(__PROXIES__)}', timeout=__CONFIG__['proxy_timeout']) as client:
            response = client.post(
            'https://discordapp.com/api/v6/invite/' + code
            )
            print(response)
    except httpx.HTTPError:
            print('Error: Could not connect to Discord')
            if response.status_code == 429:
                print(code + ' is incorrect')
                return False
            else:
                print(code + ' is correct')

def generateCode():
    code = "mantle"
    checkCode(code)
    if saveValidCodes == 'y' and True:
        saveCodes(code, 'validCodes.txt')
    if saveInvalidCodes == 'y' and False:
        saveCodes(code, 'invalidCodes.txt')
    
while True:
    generateCode()