# Divine Construction Website
## Setup
### Clone the repo into your local machine
```
git clone https://github.com/majumdersubhanu/divineconstruction.git
```
### Change directory to working directory
```
cd divineconstruction
```
### Create a virtual environment
For Linux systems
```
python3 -m venv .venv
```
For Windows systems
```
py -m venv .venv
```
### Activate the virtual environment
For Linux systems
```
source .venv/bin/activate
```
For Windows systems
```
.venv/scripts/activate
```
### Install requirements
For Linux systems
```
python3 manage.py createsuperuser
```
For Windows systems
```
py manage.py createsuperuser
```
### Create superuser
For Linux systems
```
python3 manage.py createsuperuser
```
For Windows systems
```
py manage.py createsuperuser
```
### Run the Django app
For Linux systems
```
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runapp
```
For Windows systems
```
py manage.py makemigrations

py manage.py migrate

py manage.py runapp
```
### View admin panel
Head over to `https://localhost:8000/admin` to view the admin panel.
