import random,hashlib,string
from random import randint
import subprocess



hwid = input(" [+] Enter Key: ")
#################################################################
hash1device = (hwid+"redshadow_is_here") 
result = hashlib.md5(hash1device.encode())
xxhash = result.hexdigest()
xxxhash = str(xxhash)
#################################################################33
print(" [+] Password Is: "+xxxhash)  
