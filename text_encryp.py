import random
import string 

chars =string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
plain_text = input("enter the text")
cipher_text = ""
#encrypt
for i in plain_text:
    index = chars.index(i)
    cipher_text += keys[index]
print(cipher_text)
#decrypt
plain_text =''
cipher_text = input("enter the text")
for i in cipher_text:
    index = keys.index(i)
    plain_text += chars[index]
print(plain_text)