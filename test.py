#this programe will create a folder named 'Python' into the working directory.

import os

try:
    os.system('cmd /k "mkdir Python')
except:
    print('failed!')