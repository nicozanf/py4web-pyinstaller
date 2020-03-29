# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['py4web-start.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=['bottle', 'cgitb', 'http.cookies', 'json', 'jwt', 'numbers', 'pkg_resources.py2_warn', 'pluralize', 'pydal', 'pydal.restapi',
                            'requests', 'threadsafevariable', 'yatl', 'uuid'],
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
