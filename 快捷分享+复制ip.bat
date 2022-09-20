for /f "delims=: tokens=2" %%i in ('ipconfig ^|findstr -i "ipv4"') do (set v=%%i)
set "v=%v: =%"
mshta vbscript:clipboarddata.setdata("text","http://%v%:9999")(close)
powershell -command python -m http.server 9999 -d ./share
pause