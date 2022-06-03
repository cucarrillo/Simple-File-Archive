@echo off 
pyinstaller main.py --onefile --name "SFA" --icon="resources/icon2.ico" --clean --noconfirm --distpath bin
del SFA.spec
rmdir /S /Q build
pause
