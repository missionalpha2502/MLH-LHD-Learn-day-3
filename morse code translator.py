def morse(txt):
    '''Morse code encryption and decryption'''
    
    d = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}
    translation = ''
    
    
    if txt.startswith('.') or txt.startswith('−'):
        
        d_encrypt = dict([(v, k) for k, v in d.items()])
        
        txt = txt.split(' ')
        for x in txt:
            translation += d_encrypt.get(x)
        
    
    else:
        txt = txt.upper()
        for x in txt:
            translation += d.get(x) + ' '
    return translation.strip()


print(morse('Python'))
#no software is safe

print(morse('HEY'))
#hey
print(morse('.--. -.-- - .... --- -.'))
# PYTHON
print(morse(morse('HEY')))
# HEY
