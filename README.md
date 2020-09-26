# beam-scheduler

(((requirements.txt on the way)))

cd into beam-scheduler and run the following commands (they ***should*** be the same for your os)

python -m venv env 
source env/bin/activate
python -m pip install Flask=1.1.1
python -m pip install requirements.txt

WINDOWS setup:
!# Assumed you have flask,pip,python3 commands, and virtualenv
!# If not see: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/#:~:text=%20Setup%20%201%20Step%201.%20Install%20Python%0APython,type%20in%3A%0Apip%20install%20virtualenv%0AStart%20virtualenv%0AIn%20your...%20More%20

cd into beam-scheduler directory
env\Scripts\activate
pip install -r requirements.txt --requirement=requirements.txt
set FLASK_APP=schedulerLBNL.py
flask run

go to browser and enter https://127.0.0.1:5000 

