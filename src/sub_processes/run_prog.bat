@echo off
setlocal enabledelayedexpansion

:: === 1) Get inputs from command line arguments ===
:: Usage: run_prog.bat <SIM_NAME> <FILE_NAME> <ROOT_PATH> <EXE_PATH>
set SIM_NAME=%~1
set FILE_NAME=%~2
set ROOT_PATH=%~3
set EXE_PATH=%~4

:: Debugging output
echo "Simulation Name:  %SIM_NAME%"
echo "File Name:        %FILE_NAME%"
echo "Root Path:        %ROOT_PATH%"
echo "Executable Path:  %EXE_PATH%"
echo "Simulation Path:  %SIM_PATH%"
echo.

:: Reset the out folder (delete contents but keep folder) ===
:: Combine ROOT_PATH with SIM_NAME for the full path
rmdir "%ROOT_PATH%\simulations\%SIM_NAME%\out" /S /Q
mkdir "%ROOT_PATH%\simulations\%SIM_NAME%\out"
type NUL > "%ROOT_PATH%\simulations\%SIM_NAME%\out\.gitkeep"

rmdir "%ROOT_PATH%\simulations\%SIM_NAME%\para_dats" /S /Q
mkdir "%ROOT_PATH%\simulations\%SIM_NAME%\para_dats"

rmdir "%ROOT_PATH%\simulations\%SIM_NAME%\post_process" /S /Q
mkdir "%ROOT_PATH%\simulations\%SIM_NAME%\post_process"

:: Execute simulation with piped input
(
  echo %SIM_NAME%
  echo %FILE_NAME%
) | "%EXE_PATH%"

:: Error handling
if %errorlevel% neq 0 (
    echo Simulation crashed with error code %errorlevel%.
    exit /b %errorlevel%
) else (
    echo Simulation completed successfully.
)

pause
