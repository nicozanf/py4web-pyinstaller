# py4web-pyinstaller
How to make py4web binaries for Windows and MacOS with PY3 and PyInstaller

The binaries contain Python 64 bit version 3.12.7 with all the needed modules
and the py4web in the specified version. You don't need anything else to run them!


**********************************************************************************
Please, help with testing. Write the results directly to me (nicozanf@gmail.com)
**********************************************************************************  

## Why binaries versions?

Using the binaries is much simpler and quicker if you're just learning py4web or testing your existing code with different python
versions. For a newbie, even properly installing Python could be a nightmare! Also, in this way you're sure you don't risk any damage on
your system and you can do it even if you're not an administrator.
But you should use the latest available Python version and the py4web sources (and possibly a full web server) for Production and
complex / unusual development. 

## Status

The binaries work fine, with no problem reported. The Mac version is CMD only; unfortunately the APP version is still not working.

## How to use them

Just downoad the needed zip file from the 'last_binaries' folder and uncompress it on a local folder. Open the Command Prompt / Terminal, go to that folder and run:

* for Windows: 'py4web set_password' and then 'py4web run apps' 
* for MacOs: './py4web set_password' and then './py4web run apps' 

If you prefer to build them by yourself, see the specific README [for Windows](https://github.com/nicozanf/py4web-pyinstaller/blob/master/README_win.md) and [for Mac](https://github.com/nicozanf/py4web-pyinstaller/blob/master/README_mac.md).
