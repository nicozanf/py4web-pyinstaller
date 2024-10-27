## Full MacOs build recipe
1. Install Python 3 from https://python.org (using admin priviledges and adding python.exe to the path) - I've got Python 3.12.7.
1. Install py4web as usual - I've done it in Desktop/py4web with the "Try me (from source - locally)" https://py4web.com/_documentation/static/en/chapter-03.html#installing-from-source-locally procedure. It's better to use venv or a full VM ...

1. install PyInstaller with:

           sudo -H pip3 install --upgrade pyinstaller

(I've got PyInstaller-6.11)

1. install psycopg2 with:

        pip3 install  --upgrade psycopg2-binary
        
   (if you don't need the PostgreSQL database adapter, you can avoit this - but also remove any related reference from inside the .spec file later)

1. install the dateutil module with:

        pip3 install  --upgrade python-dateutil
        
   (it's needed by some py4web tutorial, you can avoit this - but also remove any related reference from inside the .spec file later)

1. copy extras, build_py4web.py and py4web.mac.spec from this repository to Desktop/py4web

1. copy py4web-gui.py from https://github.com/nicozanf/py4web-gui to Desktop/py4web
   
1. install py4web-gui requirements with:

        pip3 install  --upgrade psutil tomlkit

1. open a Terminal and go to Desktop\py4web. Run:

        python3 build_py4web.py

If everything goes fine, you'll obtain the 64 bit binary build zipped as Desktop/py4web\py4web_osx_versionxxxx.zip.


## NOTE:

I've used MacOs 12.7.4 (Monterey)

## Current problems

If you open a py4web shell, the quit() command does not work. Use sys.exit() instead.
