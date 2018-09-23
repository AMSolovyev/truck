# Truck

The application displays the reference parameters of dump trucks, their current weight and overload value in % (how much is exceeded max.load capacity).
If the truck is not overloaded, this value is not displayed.

[Working version](/) 

The functionality of the application allows you to add:
- new models of dump trucks with their maximum load capacity
- a specific machine with the hull number and current weight



# Run local version
` ' #!bash

virtualenv -p python3 venv
source venv/bin/activate
pip install-r requirements.txt
python manage.py runserver
"`

Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)