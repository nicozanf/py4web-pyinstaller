## Windows binaries

At least on Windows 7, if you get an error stating that "api-ms-win-crt-runtime-l1-1-0.dll is missing" you have only to install
the free and official Microsoft "Visual C++ Redistributable for Visual Studio".

## Full Windows build recipe


1. Install Python 3 from https://python.org (using admin priviledges and adding python.exe to the path) - I've got Python 3.12.7.
1. Install py4web as usual - I've done it in C:\py4web\ with the "Installing from source (locally)"
   https://py4web.com/_documentation/static/en/chapter-03.html#installing-from-source-locally procedure . It's better to use venv or a full VM ...
1. install PyInstaller with:  

        pip install  --upgrade pyinstaller
        
   (I've got PyInstaller-6.11)
        
1. install the dateutil module with:

        pip install  --upgrade python-dateutil
        
   (it's needed by some py4web tutorial, you can avoit this - but also remove any related reference from inside the .spec file later)
1. install psycopg2 with:

        pip install  --upgrade psycopg2-binary
        
   (if you don't need the PostgreSQL database adapter, you can also avoid this - but also remove any related reference from inside the .spec file later)
1. copy extras, build_py4web.py, py4web-gui.win.spec and py4web.win.spec from this repository to C:\py4web\


1. copy py4web-gui.py from https://github.com/nicozanf/py4web-gui to C:\py4web\
   
1. install py4web-gui requirements with:

        pip3 install  --upgrade psutil tomlkit

1. open a CMD and go to C:\py4web. Run:

    python build_py4web.py

If everything goes fine, you'll obtain the 64 bit binary build, zipped as C:\py4web\py4web_win_versionxyz.zip.  
If you try to run it in a 32 bit Windows system, you'll correctly get a 'web2py.exe not a valid Win32 application' error message.

## Current problems

If you open a py4web shell, the quit() command does not work. Use sys.exit() or CTRL-BREAK instead.
