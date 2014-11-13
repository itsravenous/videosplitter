# -*- mode: python -*-
a = Analysis(['video-split.py'],
             pathex=['C:\\Users\\IEUser\\Desktop\\video-split'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='video-split.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               [('ffmpeg.exe', './ffmpeg.exe', 'BINARY')],
               [('icons/list-add.png', './icons/list-add.png', 'DATA')],
               [('icons/editclear.png', './icons/editclear.png', 'DATA')],
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='video-split')
