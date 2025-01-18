# -*- mode: python ; coding: utf-8 -*-

src = [
    ('src', 'src'),
    ('src/modules', 'src/modules'),
    ('src/resources', 'src/resources'),
    ('src/resources/sounds', 'src/resources/sounds'),
    ('src/modules/ras', 'src/modules/ras')
    ('README.md', 'README.md')
    ('LICENSE', 'LICENSE')
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

splash = Splash(
    'src/resources/subtitut_logo copy.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=(10, 50),
    text_size=12,
    text_color='black',
    text_default='Loading Estudy Surfing'
)

dist = DISTPATH(
    'App'
)

exe = EXE(
    pyz,
    a.scripts,
    splash,
    splash.binaries,
    a.binaries,
    a.datas,
    dist,
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
