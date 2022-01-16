@echo off

call %~dp0venv\Scripts\activate

cd %~dp0

set TOKEN=5035661923:AAEvW8yhqY4_9lmu3EYvHqMwH0jrAg-eF9g

python telegram_bot.py

pause
