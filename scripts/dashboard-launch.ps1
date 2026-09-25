$root=(Get-Location).Path
$vbs=(Resolve-Path ".\scripts\dashboard-start.vbs").Path
$url="http://127.0.0.1:8501/"
$listener=Get-NetTCPConnection -LocalPort 8501 -State Listen -ErrorAction SilentlyContinue
if(-not $listener){ Start-Process -FilePath "wscript.exe" -ArgumentList @("`"$vbs`"") -WorkingDirectory $root }
for($n=1;$n -le 45;$n++){ Start-Sleep -Seconds 1; $listener=Get-NetTCPConnection -LocalPort 8501 -State Listen -ErrorAction SilentlyContinue; if($listener){ Write-Host "DASHBOARD_STATUS=PASS" -ForegroundColor Green; Write-Host "DASHBOARD_URL=$url" -ForegroundColor Green; Start-Process $url; exit 0 } }
Write-Host "DASHBOARD_STATUS=FAIL" -ForegroundColor Red
exit 1
