@echo off
echo Deteniendo servidor anterior...
taskkill /f /im node.exe 2>nul
echo.
echo Iniciando servidor con datos actualizados...
echo.
echo La aplicacion estara disponible en: http://localhost:3000
echo.
npx serve . -p 3000

