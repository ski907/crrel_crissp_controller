@echo off
setlocal enabledelayedexpansion

:: Get the current directory where the script is run.
set "current_dir=%cd%"

:: Define the source and destination directories.
set "source_dir=%current_dir%\out"
set "destination_dir=%current_dir%\para_dats"

:: === Step 1: If para_dats exists, delete its contents but keep the folder ===
if exist "%destination_dir%" (
    for /f "delims=" %%f in ('dir "%destination_dir%" /b /a') do (
        set "file_path=%destination_dir%\%%f"
        if exist "!file_path!" (
            if exist "!file_path!\*" (
                rmdir "!file_path!" /s /q
            ) else (
                del "!file_path!"
            )
        )
    )
) else (
    mkdir "%destination_dir%"
)

:: === Step 2: Create the destination directory if it doesn't exist ===
if not exist "%destination_dir%" (
    mkdir "%destination_dir%"
)

:: === Step 3: Copy .plt files from out/ to para_dats/, renaming them to .dat ===
if exist "%source_dir%" (
    for %%f in ("%source_dir%\*.plt") do (
        set "source_file=%%f"
        set "file_name=%%~nf"
        set "destination_file=%destination_dir%\!file_name!.dat"
        copy "!source_file!" "!destination_file!"
        echo Copied and renamed: !source_file! to !destination_file!
    )
) else (
    echo Source directory "%source_dir%" does not exist.
)

:: Done
echo All .plt files have been copied and renamed to .dat in the para_dats directory.
pause
