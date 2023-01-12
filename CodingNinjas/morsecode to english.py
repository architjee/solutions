from os import *
from sys import *
from collections import *
from math import *

def morseToEnglish(morsecode):
    d = { ".-": 'a', "-...":'b', "-.-.":'c', "-..":'d', ".":'e', "..-.":'f', "--.":'g', "....":'h', "..":'i', ".---":'j', "-.-":'k', ".-..":'l', "--":'m', "-.":'n', "---":'o', ".--.":'p', "--.-":'q', ".-.":'r', "...":'s', "-":'t', "..-":'u', "...-":'v', ".--":'w', "-..-":'x', "-.--":'y', "--..":'z', "-----":'0', ".----":'1', "..---":'2', "...--":'3', "....-":'4', ".....":'5', "-....":'6', "--...":'7', "---..":'8', "----.":'9' }
    result = []
    
    for code in morsecode.split(' '):
        if code == '':
            result.append('')
            continue
        result.append(d[code])
    return ''.join(result)
    # Write your code here.