## Full MacOs build recipe
1. Install Python 3 and py4web as usual. I've done it in Desktop/py4web with the "Try me (from source)" procedure and Python 3.8.6. It's better to use venv or a full VM ...

1. install PyInstaller with:
sudo -H pip3 install --upgrade pyinstaller  (I've got PyInstaller-4.1.tar.gz )

1. copy extras, build_py4web.py and py4web.win.spec from this repository to Desktop/py4web

1. (optional, for having a full working interactive shell) change the fake site.py module included within the PyInstaller installation with the content of the files web2py.site_37.py
   from https://github.com/nicozanf/web2py-pyinstaller/blob/master/web2py.site_37.py - see comments inside that file for details. It work for Python 3.8, too.

1. open a Terminal and go to Desktop\py4web. Run:

python3 build_py4web.py

If everything goes fine, you'll obtain the 64 bit binary build zipped as Desktop/py4web\py4web_osx.zip.


## NOTE:

There is a bug (see https://github.com/pyinstaller/pyinstaller/issues/5062) with Pyinstaller and Python >= 3.7.6. After compiling, you need to run on the compiled code:   

$ sudo codesign --remove-signature Python


