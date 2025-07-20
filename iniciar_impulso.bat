@echo off
setlocal

:: Verificar permisos de administrador
net session >nul 2>&1
if %errorlevel% NEQ 0 (
    echo ⚠️ ATENCIÓN: No se está ejecutando como administrador. La elevación de prioridad podría fallar.
) else (
    echo ✅ Ejecutando como administrador.
)

:: Iniciar VM
echo 🚀 Iniciando VM...
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "Impulso"

:: Esperar que arranque el proceso
timeout /t 10 /nobreak >nul

:: Subir prioridad al proceso VirtualBoxVM con más CPU
echo ⚙️ Buscando proceso VirtualBoxVM.exe con más uso de CPU...

powershell -NoProfile -Command "`
    $p = Get-Process VirtualBoxVM | Sort-Object CPU -Descending | Select-Object -First 1; `
    Write-Host ('📌 Proceso con más uso de CPU: PID ' + $p.Id); `
    $p.PriorityClass = 'High'; `
    Write-Host ('🟢 Prioridad elevada a HIGH para PID ' + $p.Id)"

echo 🟢 Proceso finalizado.
pause
