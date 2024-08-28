from PyInstaller.utils.win32.versioninfo import VSVersionInfo, FixedFileInfo, StringFileInfo, StringStruct, StringTable, VarFileInfo, VarStruct

vers = VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(1, 1, 0, 0), 
        prodvers=(1, 1, 0, 0), 
        mask=0x3f,
        flags=0x0,
        OS=0x4,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo([
            StringTable(
                '040904B0', [
                    StringStruct('FileDescription', 'This app helps you to resize and compress images'), 
                    StringStruct('FileVersion', '1.1.0.0'),
                    StringStruct('InternalName', 'image_resizer'),
                    StringStruct('LegalCopyright', '© 2024 Taras Smetaniuk, Nestle. All rights reserved.'),
                    StringStruct('LegalTrademarks', ''),
                    StringStruct('OriginalFilename', 'image_resizer.exe'),
                    StringStruct('ProductName', 'Image Resizer'),
                    StringStruct('ProductVersion', '1.1.0.0'),
                    StringStruct('License', 'MIT License'),
                    StringStruct('Comments', 'Author: Taras Smetaniuk. GitHub: https://github.com/Smetan88/image_resizer'),
                    StringStruct('AuthorName', 'Taras Smetaniuk')
                ]
            )
        ]),
        VarFileInfo([VarStruct('Translation', [0x0409, 0x04B0])])
    ]
)

a = Analysis(
    ['image_resizer.py'],
    pathex=['.'],
    binaries=[],
    datas=[('logo.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='image_resizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='icon.ico',
    version=vers,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='image_resizer',
)