#MacOs binaries
The MacOS binaries on https://github.com/nicozanf/py4web-pyinstaller contain Python 3.7.4 64 bit with all the needed modules and the web2py in the specified version: you don't need anything else to run them on MacOS! After uncompressing the zip file, you just need to open a Terminal, goto to that folder and run './py4web-start apps'.
They were produced by me on MacOS Sierra 10.12.6 + security update 2019.001.

##Full MacOs build recipe
Install Python 3 and py4web as usual. I've done it in Desktop/py4web with the "Try me (from source)" procedure and Python 3.7.4. It's better to use venv or a full VM ...

install PyInstaller with:
sudo -H pip3 install --upgrade pyinstaller  (I've got PyInstaller-3.6.tar.gz )

copy build_py4web.py and py4web.win.spec from this repository to Desktop/py4web

open a Terminal and go to Desktop\py4web. Run:

python3 build_py4web.py

If everything goes fine, you'll obtain the 64 bit binary build zipped as Desktop/py4web\py4web_osx.zip.

