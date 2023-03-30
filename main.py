from anonfile import AnonFile
import os
import shutil
def upload(filepath):
    file_up = AnonFile()
    up = file_up.upload(filepath)
    print(up.url.geturl())
src = r'lol.txt'
dest = 'hi.py'
path = shutil.copyfile(src,dest)