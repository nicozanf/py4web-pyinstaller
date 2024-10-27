# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['py4web-gui.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=['cgitb', 'click', 'cryptography', 'http.cookies', 'json', 'jwt', 'numbers', 'ombott', 'pkg_resources.py2_warn', 'pluralize', 
                            'portalocker', 'pydal', 'pydal.restapi', 'psutil', 'psutil._psutil_windows', 'tomlkit',
                            'pydal.tools', 'pydal.tools.scheduler', 'pydal.tools.tags', 'renoir', 'requests', 'rocket3', 'threadsafevariable', 'tornado', 'yatl', 'uuid',
                            'aifc', 'asynchat', 'asyncore', 'binhex', 'chunk', 'collections.abc', 'colorama', 'colorsys', 'compileall', 'cProfile',
                            'crypt', 'Crypto', 'Crypto.Cipher.AES', 'curses.ascii',
                            'curses.panel', 'curses.textpad', 'dataclasses', 'dateutil',
                            'dbm', 'dbm.dumb', 'dbm.gnu', 'dbm.ndbm', 'encodings.idna', 'encodings.mbcs', 'encodings.utf_8_sig', 'ensurepip', 
                            'fcntl', 'filecmp', 'fileinput', 'formatter', 'fractions', 'grp',
                            'imghdr', 'json.tool', 'logging.config', 'mailbox', 'mailcap', 'modulefinder', 'msilib', 'os.path', 'pathlib', 'pickletools', 'pipes',
                            'poplib', 'posix', 'profile', 'pstats', 'psycopg2', 'pty', 'pwd', 'pyclbr', 'readline', 'resource', 'rlcompleter', 
                            'secrets', 'shelve', 'smtpd', 'sndhdr',
                            'statistics', 'struct', 'sunau', 'symbol', 'symtable', 'tabnanny', 'telnetlib', 'termios', 'timeit',
                            'trace', 'turtle', 'turtledemo', 'urllib.robotparser', 'venv', 'watchgod', 'wave', 'winreg', 'winsound', 'xdrlib', 'xml.dom',
                            'xml.dom.minidom', 'xml.dom.pulldom', 'xml.etree.ElementTree', 'xmlrpc.server', 'zipapp'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['py4web'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='py4web-gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='extras\\icons\\py4web.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='py4web-gui')
