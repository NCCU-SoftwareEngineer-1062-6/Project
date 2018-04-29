echo this will make new virtualenv and install required pip package
echo Do you want to continue
pause
virtualenv .env
.env\Scripts\activate.bat
pip install -r requirements.txt