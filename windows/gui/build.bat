pyinstaller.exe --onefile --windowed --icon=assets/logo.ico --clean main.py
xcopy assets\*.* dist\assets /e /s
pause