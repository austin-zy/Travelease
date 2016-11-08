<h1>Travelease</h1>


Travelling can be something everyone is anticipating for or might be a nightmare if missed out planning. Before going for travelling, the most headache part may come to budgeting and thinking where to go. It could be time-saving if there is a system that will gather the previous travel cases and travellers just have to provide some inputs to calculate the most similar case and an estimated cost will be produced.

Travelease is a simple yet powerful case-based reasoning system that takes in real travel cases in European countries and perform case-based searching to retrieve the most similar case. It can be used for budget calculation and hotel suggestion. The system is designed to have as simple as possible to allow anyone to perform travel case searching.


#Manual
1. Install Python 2.7 from https://www.python.org/download/releases/2.7/
2. Install pip as python package manager from https://pip.pypa.io/en/stable/installing/
3. Install package dependencies using command:
   1. pip install django
   2. pip install numpy
   3. pip install scipy
   4. pip install sklearn
   5. pip install geopy
   6. pip install csv*
   7. pip install pandas
4. Download the project file from Github: https://github.com/austin-zy/Travelease/
5. Go to the project directory in cmd and run: python manage.py runserver
6. Go to web browser and go to link: localhost:8000
7. You should click on the map to select the place you wanted to visit and fill in all blanks to proceed with prediction
8. The result will come out in a lightbox.
