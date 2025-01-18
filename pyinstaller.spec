# -*- mode: python ; coding: utf-8 -*-

src = [
    ('/src', '/src')
    ('/src/modules', '/src/modules')
    ('/src/resources', '/src/resources')
    ('/src/resources/sounds', '/src/resources/sounds')
    ('/src/modules/ras', '/src/modules/ras')
]

a = Analysis(
    ['loader.py'],
    pathex=[],
    binaries=[],
    datas=src,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Estudy Surfing',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
