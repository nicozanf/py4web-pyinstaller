#!/usr/bin/env python
# -*- coding: utf-8 -*-


from distutils.core import setup
#from gluon.import_all import base_modules, contributed_modules
#from gluon.fileutils import readlines_file
from glob import glob
import os
import shutil
import sys
import re
import zipfile
import subprocess
import platform


USAGE = """
build_py4web - make py4web Windows and MacOS binaries with pyinstaller 

Usage:
    Install the pyinstaller program, copy this file (plus py4web.*.spec files) 
    to py4web root folder and run:
    
    python build_py4web.py
    
    (tested with python 3.7.4 with PyInstaller 3.6)
"""
BUILD_DEBUG = False
"""
If BUILD_DEBUG is set to False, no gluon modules will be embedded inside the binary py4web.exe. 
    Thus, you can easily update the build version by changing the gluon folder inside the resulting ZIP file.
In case of problem , set BUILD_DEBUG to True. Then all the gluon modules will be analyzed and embedded, too.
    You can later analyze the .exe with 'pyi-archive_viewer py4web-start.exe' and then 'o PYZ-00.pyz'
    in order to check for missing system modules to be manually inserted in the SPEC file
 """

if len(sys.argv) != 1 or not os.path.isfile('py4web-start.py'):
    print(USAGE)
    sys.exit(1)
os_version = platform.system()
if os_version not in ('Windows', 'Darwin'):
    print('Unsupported system: %s' % os_version)
    sys.exit(1)


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

# borrowed from http://bytes.com/topic/python/answers/851018-how-zip-directory-python-using-zipfile


def recursive_zip(zipf, directory, folder=""):
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            zipf.write(os.path.join(directory, item), folder + os.sep + item)
        elif os.path.isdir(os.path.join(directory, item)):
            recursive_zip(
                zipf, os.path.join(directory, item), folder + os.sep + item)


# Python base version
python_version = sys.version_info[:3]

# py4web version
from py4web import __version__
py4web_version = __version__


if os_version == 'Windows':
    print("\nBuilding binary py4web for Windows\n")
    if BUILD_DEBUG: # debug only
        subprocess.call('pyinstaller --clean  --icon=extras/icons/py4web.ico \
                        --hidden-import=site-packages --hidden-import=gluon.packages.dal.pydal \
                        --hidden-import=gluon.packages.yatl.yatl py4web-start.py')
        zip_filename = 'py4web_win_debug'
    else: # normal run    
        subprocess.call('pyinstaller --clean  py4web-start.win.spec')
        zip_filename = 'py4web_win_' + py4web_version

    source = 'dist/py4web-start/'
    for files in os.listdir(source):
        shutil.move(os.path.join(source, files), 'dist')
    shutil.rmtree(source)
    os.unlink('dist/py4web-start.exe.manifest')

    bin_folders = ['dist',]


elif os_version == 'Darwin':
    print("\nBuilding binary py4web for MacOS\n")

    if BUILD_DEBUG: #debug only    
        subprocess.call("pyinstaller --clean --icon=extras/icons/py4web.icns --hidden-import=gluon.packages.dal.pydal  --hidden-import=gluon.packages.yatl.yatl \
                        --hidden-import=site-packages --windowed py4web.py", shell=True)
        zip_filename = 'py4web_osx_debug'
    else: # normal run
        subprocess.call("pyinstaller --clean py4web-start.mac.spec", shell=True)
        # cleanup + move binary files to dist folder
        #shutil.rmtree(os.path.join('dist', 'py4web'))
        shutil.rmtree('build')
        zip_filename = 'py4web_osx_'  + py4web_version

    shutil.move((os.path.join('dist', 'py4web-start')),(os.path.join('dist', 'py4web_cmd')))
    bin_folders = [(os.path.join('dist', 'py4web_cmd'))]

print("\npy4web binary successfully built!\n")

# add data_files
for req in ['README.md', 'requirements.txt']:
    for bin_folder in bin_folders:
        shutil.copy(req, os.path.join(bin_folder, req))
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
        
print("\nPreparing package ...")
# misc
for folders in ['py4web', 'extras', 'deployment_tools', 'apps', 'tests']:
    for bin_folder in bin_folders:
        shutil.copytree(folders, os.path.join(bin_folder, folders))
        if not os.path.exists(os.path.join(bin_folder, 'logs')):
             os.mkdir(os.path.join(bin_folder, 'logs'))


# create a py4web folder & copy dist's files into it
shutil.copytree('dist', 'zip_temp/py4web')
# create zip file
zipf = zipfile.ZipFile(zip_filename + ".zip",
                        "w", compression=zipfile.ZIP_DEFLATED)
# just temp so the py4web directory is included in our zip file
path = 'zip_temp'
# leave the first folder as None, as path is root.
recursive_zip(zipf, path)
zipf.close()
shutil.rmtree('zip_temp')
shutil.rmtree('dist')

print('... Done!\n')
print("\n\nYour binary version of py4web can be found in " + \
    zip_filename + ".zip")
print("You may extract the archive anywhere and then run py4web without worrying about module dependencies")
print("\nEnjoy binary py4web " + py4web_version + "\n with embedded Python " + sys.version + "\n")
