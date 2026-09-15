@echo off
REM ---------------------------------------------------------------------------
REM Build a standalone Windows executable: dist\pinger.exe
REM
REM Prerequisites (run once, from this folder):
REM   venv_create.bat                 - create + activate the project venv
REM   venv_install_requirements.bat   - install dependencies (incl. PyInstaller)
REM ---------------------------------------------------------------------------

setlocal
set "PYTHON=venv\Scripts\python.exe"

if not exist "%PYTHON%" (
    echo [build] Project venv not found at "%PYTHON%".
    echo [build] Run venv_create.bat then venv_install_requirements.bat first.
    exit /b 1
)

"%PYTHON%" -m PyInstaller --noconfirm --clean --onefile --console --name pinger --specpath build src\main.py
if errorlevel 1 (
    echo [build] PyInstaller build failed.
    exit /b 1
)

echo.
echo [build] Done. Executable: dist\pinger.exe
endlocal
