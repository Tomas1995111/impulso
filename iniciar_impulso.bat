@echo off
setlocal

cd /d "%~dp0"

:: Verificar permisos de administrador
net session >nul 2>&1
if %errorlevel% NEQ 0 (
    echo ⚠️ No admin
) else (
    echo ✅ Ejecutando como admin
)

:: Iniciar VM
echo 🚀 Iniciando VM...
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "Impulso" --type headless

:: Esperar que arranque el proceso
timeout /t 10 /nobreak >nul

:: Subir prioridad
echo 🔎 Ajustando prioridad...
powershell -NoProfile -Command "try {
    $p = Get-Process VirtualBoxVM | Sort-Object CPU -Descending | Select-Object -First 1
    $p.PriorityClass = 'High'
    Write-Host ('🟢 Prioridad elevada a HIGH para PID ' + $p.Id)
} catch {
    Write-Host '❌ Error elevando prioridad'
}"

exit
