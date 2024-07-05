@echo off

start "" http:127.0.0.1:5000

rem Open a seperate command prompt window 
start cmd /k "cd \ai\kis-drivers-ed && .venv\Scripts\activate.bat && app.py"


