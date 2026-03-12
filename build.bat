@echo off
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Gerando o executavel...
pyinstaller --onefile --windowed --name wallpaper_overlay wallpaper_overlay.py

echo.
echo Pronto! O executavel esta em: dist\wallpaper_overlay.exe
pause
