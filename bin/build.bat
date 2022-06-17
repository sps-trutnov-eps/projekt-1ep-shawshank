rmdir /S /Q build
rmdir /S /Q dist

py -m PyInstaller build.spec

