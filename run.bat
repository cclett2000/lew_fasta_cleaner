@echo off

rem CHECK FOR PYTHON BEFORE PROGRAM RUN
:PY_CHECK
    echo Checking for Python...
    python --version | find /v "Python"	>nul 2>nul && (goto :PY_NOT_FOUND)
    python --version | find "Python"	>nul 2>nul && (goto :PY_FOUND)
    goto :EOF

rem TAKE USER TO PYTHON WEBPAGE TO DOWNLOAD AND INSTALL PYTHON
:PY_NOT_FOUND
    echo Python not detected, taking you to download page...
    @ pause
    start "" https://www.python.org/downloads/
    goto :EOF

rem PYTHON FOUND; PROCEED WITH RUNNING THE PROGRAM
:PY_FOUND
    echo Python detected!
    echo.
    @ pause
    python %~dp0scripts\run.py
    @pause

rem ######################################################################

rem Link(s) that helped:
rem	- https://stackoverflow.com/a/60815188