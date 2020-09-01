# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['py4web-start.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=['bottle', 'cgitb', 'click', 'http.cookies', 'json', 'jwt', 'numbers', 'pkg_resources.py2_warn', 'pluralize', 'pydal', 'pydal.restapi',
                            'requests', 'threadsafevariable', 'yatl', 'uuid',
                            'aifc', 'asynchat', 'asyncore', 'binhex', 'chunk', 'collections.abc', 'colorsys', 'compileall', 'cProfile', 'crypt', 'curses.ascii', 'curses.panel', 'curses.textpad', 'dataclasses',
                            'dbm', 'dbm.dumb', 'dbm.gnu', 'dbm.ndbm', 'encodings.idna', 'encodings.mbcs', 'encodings.utf_8_sig', 'ensurepip', 'fcntl', 'filecmp', 'fileinput', 'formatter', 'fractions', 'grp',
                            'imghdr', 'json.tool', 'logging.config', 'mailbox', 'mailcap', 'modulefinder', 'msilib', 'os.path', 'pathlib', 'pickletools', 'pipes',
                            'poplib', 'posix', 'profile', 'pstats', 'pty', 'pwd', 'pyclbr', 'readline', 'resource', 'rlcompleter', 'secrets', 'shelve', 'smtpd', 'sndhdr',
                            'statistics', 'struct', 'sunau', 'symbol', 'symtable', 'tabnanny', 'telnetlib', 'termios', 'timeit',
                            'trace', 'turtle', 'turtledemo', 'urllib.robotparser', 'venv', 'wave', 'winreg', 'winsound', 'xdrlib', 'xml.dom',
                            'xml.dom.minidom', 'xml.dom.pulldom', 'xml.etree.ElementTree',  'xmlrpc.server', 'zipapp'],
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
          name='py4web-start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='extras\\icons\\py4web.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='py4web-start')
