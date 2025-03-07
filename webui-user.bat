@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=

@REM  --models-dir
@REM  --lora-dir

call webui.bat %COMMANDLINE_ARGS%
