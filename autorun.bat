@echo off
setlocal EnableDelayedExpansion
title autorunserver

:menu
cls
echo AutoRunServer
echo --------------------
echo 1. Start from zero (create a new venv and install all requirements)
echo 2. Start Django (Assume Django and any other libraries are already installed)
echo 3. Exit
echo.
set /p choice="Your choice: "
if "%choice%"=="1" goto A
if "%choice%"=="2" goto B
if "%choice%"=="3" exit
goto menu


:A
REM pindah directory
cd %~dp0
REM membuat virtual environment
python -m venv .venv
REM mengaktifkan venv
cd .venv/Scripts/
call Activate.bat
cd ../../
pause
REM menginstal beberapa library yang diperlukan
pip install -r requirements.txt

:B
echo.
set lib[0].name=Django              
set lib[1].name=requests            
set lib[2].name=mysqlclient         
set lib[3].name=djangorestframework 
REM memastikan library yang dibutuhkan terinstall
echo Checking requirements..
for /L %%A in (0 1 3) do (
    call pip show %%lib[%%A].name%% > nul

    if errorlevel 1 (
        echo Installing, please wait..
        call pip install %%lib[%%A].name%%
    ) else (
        call echo Library %%lib[%%A].name%% installed
    )
)


:C
REM mengaktifkan mysql
echo.
echo Follow this steps : 
echo - Start your XAMPP Control Panel and activate MySQL module
echo - Go to localhost/phpmyadmin webpage and create a new database called 'tjp'
echo - If it's done, press any key
pause

:D
REM mulai django
echo.
echo Starting Django, please wait..
cd %~dp0/fast_print
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

endlocal