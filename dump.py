import os
os.system('xdg-open https://chat.whatsapp.com/G1wtAl2gjsg0N7pimK2RHH')
os.system('git pull')
from platform import uname
bit = uname().machine.lower()
if "aarch" ==bit:
  os.system('chmod 777 dump;./dump')
else:
  exit('\n Sorry Only 64 bit is Supported This Tools! ')
