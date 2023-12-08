@echo off

:: Backup old data
rename data data_old

:: Create new data directory
xcopy /E /I /Y backup data
rd /s /q data\test
for /d %%i in (data_old\*) do (
    if /I "%%~nxi" neq "mysql" (
        if /I "%%~nxi" neq "performance_schema" (
            if /I "%%~nxi" neq "phpmyadmin" (
                xcopy "data_old\%%i" data /E /I /Y
            )
        )
    )
)
copy data_old\ibdata1 data\ibdata1

:: Notify user
echo Finished repairing MySQL data
echo Previous data is located at data_old
