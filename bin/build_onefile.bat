rmdir /S /Q build
rmdir /S /Q dist

pyinstaller build_onefile.spec

xcopy /i /s ..\data .\dist\data
xcopy /i /s ..\src\minihry .\dist\minihry
