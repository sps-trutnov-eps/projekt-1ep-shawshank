rmdir /S /Q build
rmdir /S /Q dist

py -m PyInstaller build_onefile.spec

xcopy /i /s ..\data .\dist\data
xcopy /i /s ..\src\minihry .\dist\minihry

