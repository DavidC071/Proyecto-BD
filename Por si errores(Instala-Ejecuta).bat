@echo off
cd /d "%~dp0"

echo Iniciando proyecto...

IF NOT EXIST venv (
    echo Creando entorno virtual...
    py -m venv venv
)

call venv\Scripts\activate

echo Activando entorno virtual...

IF EXIST requirements.txt (
    echo Instalando dependencias...
    pip install -r requirements.txt
)

echo Ejecutando programa...
py src/Main.py

pause