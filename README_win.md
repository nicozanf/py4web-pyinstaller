## Windows binaries

At least on Windows 7, if you get an error stating that "api-ms-win-crt-runtime-l1-1-0.dll is missing" you have only to install
the free and official "Visual C++ Redistributable for Visual Studio" as described in point 7


## Full Windows build recipe


1. Install Python 3 and py4web as usual. I've done it in C:\py4web\ with the "Try me (from source)" procedure and Python 3.7.4. It's better to use venv or a full VM ...
1. install PyInstaller with:  
        pip install  --upgrade pyinstaller  (I've got PyInstaller-3.6.tar.gz )  
1. copy build_py4web.py and py4web.win.spec from this repository to C:\py4web\  
1. open a CMD and go to C:\py4web. Run:

    python build_py4web.py

If everything goes fine, you'll obtain the 64 bit binary build zipped as C:\py4web\py4web_win.zip.  
If you try to run it in a 32 bit Windows system, you'll correctly get a 'web2py.exe not a valid Win32 application' error message.


## Current problems

It seems that the Edge browser doesn't like the binary in my VM, and all the VM gets stuck for minutes at the first run. Other browsers are fine...
