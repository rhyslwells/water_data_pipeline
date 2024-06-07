@echo off
setlocal enabledelayedexpansion

rem List of database files
set databases=GMMC-2020-M.db
@REM  GMMC-2021-M.db GMMC-2022-M.db GMMC-2023-M.db GMMC-2024-M.db

rem SQL script file
set sql_script=schema.sql

rem Loop through each database and apply the SQL script
for %%d in (%databases%) do (
    echo Applying schema to %%d

    rem Get the table name (GMMC-2020-M) from the database filename
    set db=%%d
    set table_name=!db:~0,-4!

    rem Replace the placeholder with the actual table name and execute the script
    call :apply_schema "!table_name!" %%d
)

echo Schema applied to all databases.
endlocal
goto :eof

:apply_schema
setlocal
set table_name=%~1
set db=%~2

rem Create a temporary SQL script with the table name replaced
set temp_sql_script=temp_schema.sql
type %sql_script% | sed "s/<table_name>/%table_name%/g" > %temp_sql_script%

rem Execute the temporary SQL script
sqlite3 %db% < %temp_sql_script%

rem Clean up the temporary SQL script
del %temp_sql_script%

endlocal
goto :eof
