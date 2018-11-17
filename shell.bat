@echo off
title Halite

rem
rem  To run this at startup, use this as your shortcut target:
rem  %windir%\system32\cmd.exe /k c:\path\to\project\shell.bat
rem

pushd .
call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
popd

set _NO_DEBUG_HEAP=1

rem
rem Make sure this startup bat fie exists
rem %computername% and other system wide variables set here
rem
pushd .
call "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\startup.bat"
popd

call activate ml
