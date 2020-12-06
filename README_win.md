## Windows binaries

At least on Windows 7, if you get an error stating that "api-ms-win-crt-runtime-l1-1-0.dll is missing" you have only to install
the free and official "Visual C++ Redistributable for Visual Studio" as described in point 7


## Full Windows build recipe


1. Install Python 3 and py4web as usual. I've done it in C:\py4web\ with the "Try me (from source)" procedure and Python 3.8.6. It's better to use venv or a full VM ...
1. install PyInstaller with:  
        pip install  --upgrade pyinstaller  (I've got PyInstaller-4.1.tar.gz )  
1. copy extras, build_py4web.py and py4web.win.spec from this repository to C:\py4web\
1. (optional, for having a full working interactive shell) change the fake site.py module included within the PyInstaller installation with the content of the files web2py.site_37.py 
   from https://github.com/nicozanf/web2py-pyinstaller/blob/master/web2py.site_37.py - see comments inside that file for details. It work for Python 3.8, too.
1. open a CMD and go to C:\py4web. Run:

    python build_py4web.py

If everything goes fine, you'll obtain the 64 bit binary build zipped as C:\py4web\py4web_win.zip.  
If you try to run it in a 32 bit Windows system, you'll correctly get a 'web2py.exe not a valid Win32 application' error message.


## Current problems

None