@echo off

rem ✅ Set unquoted ADB path
set ADB_PATH=C:\platform-tools-latest-windows (2)\platform-tools\adb.exe

echo Disconnecting old connections...
"%ADB_PATH%" disconnect

echo Setting up connected device...
"%ADB_PATH%" tcpip 5555

echo Waiting for device to initialize...
timeout /t 3 > nul

rem ✅ Get the device's local IP address
FOR /F "tokens=2" %%G IN ('"%ADB_PATH%" shell ip addr show wlan0 ^| find "inet "') DO set ipfull=%%G
FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G

echo Connecting to device with IP: %ip%
"%ADB_PATH%" connect %ip%

echo Restarting ADB server...
"%ADB_PATH%" kill-server
"%ADB_PATH%" start-server

rem ✅ Optional: Hardcoded fallback IP
set DEVICE_IP=192.168.29.71
set ADB_PORT=5555
echo Connecting again to %DEVICE_IP%:%ADB_PORT%
"%ADB_PATH%" connect %DEVICE_IP%:%ADB_PORT%

echo ✅ Done!
pause
