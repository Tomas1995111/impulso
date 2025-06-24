@echo off
set "LOGFILE=log_sincronizacion.txt"
echo [%date% %time%] Sincronizando hora... >> "%~dp0%LOGFILE%"
net stop w32time
w32tm /config /manualpeerlist:"time.cloudflare.com" /syncfromflags:manual /reliable:YES /update
net start w32time
w32tm /resync >> "%~dp0%LOGFILE%" 2>&1
echo Hora sincronizada. >> "%~dp0%LOGFILE%"