@echo off
echo ========================================
echo    OFFLINE RAG SYSTEM STATUS CHECK
echo ========================================
echo.

echo Checking components...
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [✓] Python is installed
    python --version
) else (
    echo [✗] Python not found
)

:: Check Ollama
ollama --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [✓] Ollama is installed
    ollama --version
) else (
    echo [✗] Ollama not installed
)

:: Check if model is downloaded
echo.
ollama list 2>nul | findstr /i "llama2" >nul
if %errorlevel% equ 0 (
    echo [✓] Llama2 model is downloaded (OFFLINE READY)
) else (
    echo [✗] Llama2 model not downloaded (needs one-time download)
)

:: Check if packages are installed
echo.
python -c "import streamlit; print('[✓] Streamlit installed')" 2>nul || echo [✗] Streamlit not installed
python -c "import langchain; print('[✓] Langchain installed')" 2>nul || echo [✗] Langchain not installed
python -c "import faiss; print('[✓] FAISS installed')" 2>nul || echo [✗] FAISS not installed

:: Check directories
echo.
if exist "rag_storage" (
    echo [✓] Storage directory exists
) else (
    echo [i] Storage directory will be created on first use
)

echo.
echo ========================================
echo.
pause