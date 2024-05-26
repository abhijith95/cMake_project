@REM use REM to add comments in the batch file. Writing @echo off will only display the output in the CLI.
@echo off
@REM %~dp0 refers to the current directory where the batch script is located
SETLOCAL EnableDelayedExpansion

@REM when using the If statement the bracket has to be in the same line as the keyword if. 
@REM when using else statement else has to be on the same line as the bracket which ends the if statement

@REM setting the index to zero. !!! DO NOT GIVE SPACE AROUND THE EQUAL SIGN !!!
set inputArgument=%~1
set /A found_character_flag=0

if [!inputArgument!] == [] ( goto show_options ) else ( goto continue_on)
:show_options
    echo C - clear the existing build folder
    echo B - build the exe of main.cpp
    @REM eof specifies end of file so it will go there and do nothing
    goto :eof

@REM variable:<character>=<replacement value> replaces the character found in the variable with the replacement value 
@REM Below if the character exists in the string it will be replaced with empty character. If the character is not present
@REM in the string then string before and after removal will be the same, if its not equal then we know that character is present. set "CLEAN = TRUE"

:continue_on
if "!inputArgument!" NEQ "!inputArgument:C=!" set "CLEAN=TRUE"
if "!inputArgument!" NEQ "!inputArgument:B=!" set "EXE_BUILD=TRUE"
if "!inputArgument!" NEQ "!inputArgument:E=!" set "EMUL_BUILD=TRUE"

if !CLEAN!==TRUE (
                    echo Deleting the build folder
                    @REM /S refers to deleting the entire directory and /Q does it silently without prompting the user for permission
                    @RD /S /Q %~dp0\out\build %~dp0\out\emul
                    md %~dp0\out\build %~dp0\out\emul
                    set /A found_character_flag=1
                )
if !EXE_BUILD!==TRUE (                        
                        echo *****************************************
                        echo Building software
                        echo *****************************************

                        @REM -D will help in setting variable to cmake and we can use such variable in CMakeLists.txt file 
                        cmake -S %~dp0 -B %~dp0\out\build -D BUILD_TYPE_CONFIG=EXEC_BUILD

                        echo *****************************************
                        echo Installing the build image
                        echo *****************************************
                        cmake --build %~dp0\out\build
                        echo *****************************************
                        echo Build ready!
                        echo *****************************************
                        set /A found_character_flag=1
                    ) 
if !EMUL_BUILD!==TRUE (                        
                        echo *****************************************
                        echo Building emulator dll
                        echo *****************************************

                        @REM -D will help in setting variable to cmake and we can use such variable in CMakeLists.txt file 
                        cmake -S %~dp0 -B %~dp0\out\emul -D BUILD_TYPE_CONFIG=EMULATOR_BUILD -DCMAKE_BUILD_TYPE=Debug

                        echo *****************************************
                        echo Installing the build image
                        echo *****************************************
                        cmake --build %~dp0\out\emul
                        echo *****************************************
                        echo Build ready!
                        echo *****************************************
                        set /A found_character_flag=1
                    ) 

if !found_character_flag!==0 (    
                                echo Cannot find the command. Use only following characters
                                echo *****************************************
                                goto show_options
                            )