@echo off

:: Check for pip and proceed if found
python -m pip --version > nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo pip is not installed. Please install Python and ensure pip is added to the PATH.
    exit /b
)

echo Checking and installing required Python packages...

:: Read each line in requirements.txt
for /F "delims==" %%i in (requirements.txt) do (
    python -m pip show %%i > nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo Installing %%i...
        python -m pip install %%i
        if %ERRORLEVEL% neq 0 (
            echo Failed to install %%i.
            pause
            exit /b
        )
    ) else (
        echo %%i is already installed.
    )
)

echo All required packages are installed.

echo Running Main Simulation...
python MainSimulation.py >nul 2>nul
pause