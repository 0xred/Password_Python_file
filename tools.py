import random,hashlib,string
from random import randint
import subprocess



hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
result = hashlib.md5(hwid.encode())
hashx = result.hexdigest() 
#################################################################
hash1device = (hashx+"redshadow_is_here") 
result = hashlib.md5(hash1device.encode())
xxhash = result.hexdigest()
xxxhash = str(xxhash)
#################################################################33
print(" [+] Your Key: "+hashx) 
pessx = input(" [+] Enter Pass: ") 

if pessx == xxxhash: 
    print('  successfully Login \n Welcome Bro :) ')
else:
    print(' Error Password ... Try Again ')
    
