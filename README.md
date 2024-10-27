# py4web-pyinstaller
How to make py4web binaries for Windows and MacOS with PY3 and PyInstaller

The binaries contain Python 64 bit version 3.12.7 with all the needed modules
and the py4web + py4web-gui programs in the specified version. You don't need anything else to run them!

# program sources

* py4web: see https://github.com/web2py/py4web
* py4web-gui: see https://github.com/nicozanf/py4web-gui

## Why binaries versions?

Using the binaries is much simpler and quicker if you're just learning py4web or testing your existing code with different python
versions. For a newbie, even properly installing Python could be a nightmare! Also, in this way you're sure you don't risk any damage on
your system and you can do it even if you're not an administrator.
But you should use the latest available Python version and the py4web sources (and possibly a full web server) for Production and
complex / unusual development.

They surely makes the experience of installing and running py4web even much simpler and enjoyable.

## Status

The binaries work fine, with no big problem reported. Finally, the MacOs version is a standart Mac app!

Small issues:
* Windows: you cannot run new instances without the default check "Show py4web output on console"
* python sources are surely not an example of a good programming style ;-)

## How to use them

Just downoad the needed zip file from the 'last_binaries' folder and uncompress it on a local folder. Then, simply run the py4web-gui application!

If you prefer to use the Command Prompt / Terminal, go to that folder (on MacOs, also inside the app with 'cd py4web-gui.app/Contents' ).

The run:

* for Windows: 'py4web run apps' 
* for MacOs: ' './py4web run apps' 

If you prefer to build them by yourself, see the specific README [for Windows](https://github.com/nicozanf/py4web-pyinstaller/blob/master/README_win.md) and [for Mac](https://github.com/nicozanf/py4web-pyinstaller/blob/master/README_mac.md).
