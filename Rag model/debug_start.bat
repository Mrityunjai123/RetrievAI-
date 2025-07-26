@echo off
echo Starting Debug Mode...
cd /d "D:\PDF_reader"

echo.
echo Current directory:
cd

echo.
echo Checking Python...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit
)

echo.
echo Setting environment variable...
set TF_USE_LEGACY_KERAS=1

echo.
echo Starting Streamlit...
python -m streamlit run streamlit_app.py

echo.
echo If you see this, Streamlit stopped.
pause