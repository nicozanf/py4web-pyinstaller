#!/usr/bin/env python
# -*- coding: utf-8 -*-

# build_py4web.py
#

# v 2.5 20241103 nicozanf@gmail.com
# using make_archive instead of custom recursive_zip
# changes for py4web-gui
# changes for  _internal changes on Pyinstaller 6.0


from distutils.core import setup
#from gluon.import_all import base_modules, contributed_modules
#from gluon.fileutils import readlines_file
from glob import glob
import os
import shutil
import sys
import re
import subprocess
import platform


USAGE = """
build_py4web - make py4web Windows and MacOS binaries with pyinstaller 

Usage:
    Install the pyinstaller program, copy this file (plus py4web.*.spec files) 
    to py4web root folder and run:
    
    python build_py4web.py
    
    (tested with python 3.12.7 with PyInstaller 6.11.0)
    
"""


def zip_with_symlinks(folder_to_compress, output_zipfile, subfolder=None):
    if subfolder:
        subprocess.run(["zip", "-r", "-y", output_zipfile, folder_to_compress], cwd=subfolder, check=True)
    else:
        subprocess.run(["zip", "-r", "-y", output_zipfile, folder_to_compress], check=True)


#cleanup old runs if present
if os.path.exists('dist'):
    shutil.rmtree('dist')

if len(sys.argv) != 1 or not os.path.isfile('py4web.py'):
    print(USAGE)
    sys.exit(1)
os_version = platform.system()
if os_version not in ('Windows', 'Darwin'):
    print('Unsupported system: %s' % os_version)
    sys.exit(1)


# Python base version
python_version = sys.version_info[:3]

# py4web version
from py4web import __version__
py4web_version = __version__


if os_version == 'Windows':
    print("\nBuilding binary py4web-gui for Windows\n")
    subprocess.call('pyinstaller --clean  py4web-gui.win.spec')

    print("\n\nBuilding binary py4web-gui for Windows\n")
    subprocess.call('pyinstaller --clean  py4web.win.spec')

    zip_filename = 'py4web_win_' + py4web_version
    if os.path.exists(zip_filename):
        os.unlink(zip_filename)

    bin_folder = [(os.path.join('dist', 'py4web'))]

elif os_version == 'Darwin':
    print("\nBuilding binary py4web-gui for MacOS\n")


    subprocess.call("pyinstaller --clean py4web-gui.mac.spec", shell=True)
    shutil.rmtree('build')
    #shutil.move((os.path.join('dist', 'py4web-gui.app')),(os.path.join('extras', 'py4web_cmd')))
    
    print("\nBuilding binary py4web for MacOS\n")
    subprocess.call("pyinstaller --clean py4web.mac.spec", shell=True)
    # cleanup + move binary files to dist folder
    shutil.rmtree('build')
    
    zip_filename = 'py4web_osx_'  + py4web_version
    if os.path.exists(zip_filename):
        os.unlink(zip_filename)

    # shutil.move((os.path.join('dist', 'py4web')),(os.path.join('dist', 'py4web_cmd')))
    
    bin_folder = [(os.path.join('dist', 'py4web'))]
    shutil.rmtree(os.path.join('dist', 'py4web_app.app')) # app is not working
    
    os.makedirs('dist/py4web_cmd/docs', exist_ok=True)



print("\npy4web binary successfully built!\n")

# add data_files
for req in ['README.rst', 'CONTRIBUTORS.rst', 'LICENSE.md',]:
    shutil.copy(req, os.path.join(*bin_folder, req))
# cleanup unuseful binary cache
for dirpath, dirnames, files in os.walk('.'):
    if dirpath.endswith('__pycache__'):
        print('Deleting cached binary directory : %s' % dirpath)
        shutil.rmtree(dirpath)
for dirpath, dirnames, files in os.walk('.'):
    for file in files:
        if file.endswith('.pyc'):
            print('Deleting cached binary file : %s' % file)
            os.unlink(os.path.join(dirpath, file))
        
print("\nPreparing ZIP package ...")
# misc
internal = [(os.path.join(*bin_folder, '_internal'))] # this is the subfolder with all binaries on Pyinstaller >= 6.0

shutil.copytree('py4web', os.path.join(*internal, 'py4web'), symlinks=True)
shutil.copytree('extras', os.path.join(*internal, 'extras'), symlinks=True)
shutil.copytree('apps', os.path.join(*bin_folder, 'apps'), symlinks=True)

shutil.copytree(os.path.join('docs', 'images'), os.path.join('dist', 'py4web','docs', 'images'), symlinks=True)

if os_version == 'Darwin':
    shutil.copytree(os.path.join('dist', 'py4web-gui.app'), os.path.join('dist', 'py4web', 'py4web-gui.app'), symlinks=True)
    for req in ['README.rst', 'CONTRIBUTORS.rst', 'LICENSE.md', '_internal', 'apps', 'docs', 'py4web', ]:
        shutil.move((os.path.join('dist', 'py4web', req)),(os.path.join('dist', 'py4web', 'py4web-gui.app', 'Contents')))
    shutil.move((os.path.join('dist', 'py4web', 'py4web-gui.app', 'Contents', '_internal', 'py4web')),(os.path.join('dist', 'py4web', 'py4web-gui.app', 'Contents', 'Frameworks')))
else:
    shutil.copy(os.path.join('dist', 'py4web-gui', 'py4web-gui.exe'), os.path.join('dist', 'py4web', 'py4web-gui.exe'))

# create a py4web folder & copy dist's files into it
shutil.copytree('dist/py4web', 'zip_temp/py4web', symlinks=True)

if os_version == 'Darwin':
    int_src = os.path.join('zip_temp',  'py4web', 'py4web-gui.app', 'Contents', '_internal')
    int_des = os.path.join('zip_temp',  'py4web', 'py4web-gui.app', 'Contents', 'Frameworks')

     
    shutil.rmtree(int_src)

    subprocess.call("ln -s Frameworks zip_temp/py4web/py4web-gui.app/Contents/_internal", shell=True)


# create zip file
if os_version == 'Darwin':
    # on Mac shutil.make_archive does not preserve symlinks
    zip_with_symlinks('py4web', zip_filename + '.zip', subfolder='zip_temp')
    shutil.move((os.path.join('zip_temp', zip_filename + '.zip')), zip_filename + '.zip')
else:
    shutil.make_archive(zip_filename, 'zip', 'zip_temp')

shutil.rmtree('zip_temp')
shutil.rmtree('dist')

print('... Done!\n')
print("\n\nYour binary version of py4web can be found in " + \
    zip_filename + ".zip")
print("You may extract the archive anywhere and then run py4web without worrying about module dependencies")
print("\nEnjoy binary py4web " + py4web_version + "\n with embedded Python " + sys.version + "\n")

