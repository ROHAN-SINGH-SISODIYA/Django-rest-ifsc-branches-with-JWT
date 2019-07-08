Django-rest-ifsc-branches with JWT
A RESTful API written in Django to get any branch details using ifsc code and find all the branches of a bank in a Indian city.

##Run
   
   $ python manage.py runserver

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```

You can install httpie using pip:
```
    pip install httpie
```

Only authenticated users can use the API services, for that reason if we try this:
```
	http  http://127.0.0.1:8000/ifsc/ALLA0210804
```
we get:
```
 {  "detail":  "You must be authenticated"  }
```
Instead, if we try to access with credentials:
```
	curl -H "Authorization:Token 97e0503454c871b73d52e0bacee046c8611ed5de"   http://127.0.0.1:8000/branches/BHOPAL/ALLAHABAD%20BANK 
	
	##Run On Heroku Server
	
	curl -H "Authorization:Token 97e0503454c871b73d52e0bacee046c8611ed5de" 
		https://fylehq-api.herokuapp.com/branches/BHOPAL/ALLAHABAD%20BANK 
```

## Login and Tokens

To get a token first we have to login
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="12345"
```
after that, we get the token
```  
{
    "key": "97e0503454c871b73d52e0bacee046c8611ed5de"
    
    validity upto 5 days
}
```
### Curl Commands

curl -H "Authorization:Token key" http://localhost:8000/ifsc/{ifsccode} 

curl -H "Authorization:Token key" http://localhost:8000/branches/{city}/{bank-name} 

### with heroku 

curl -H "Authorization:Token key" https://fylehq-api.herokuapp.com/ifsc/{ifsccode}

curl -H "Authorization:Token key" https://fylehq-api.herokuapp.com/branches/{city}/{bank-name} 

in your browser to get started.