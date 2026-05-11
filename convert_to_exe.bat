@echo off

call venv\Scripts\activate.bat

echo ==============================
echo   Cleaning previous builds
echo ==============================

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec

echo.
echo ==============================
echo   Installing dependencies
echo ==============================

pip install -r requirements.txt

echo.
echo ==============================
echo   Building executables
echo ==============================
venv\Scripts\pyinstaller --noconfirm --clean --onefile --noconsole --name Text_Swap app.py

echo.
echo ==============================
echo   Build complete!
echo ==============================
