@echo off
echo --- PDF Merger Setup ---

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in your PATH.
    echo Please install Python from python.org and try again.
    pause
    exit /b
)

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
call .venv\Scripts\activate

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
if exist "requirements.txt" (
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Warning: requirements.txt not found!
)

echo.
echo Setup complete!
echo You can now run the tool using 'run.bat'.
pause
