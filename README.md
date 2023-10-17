# Start Website (First time)
- instlal python 3.10 virtual environment
- activate virtual environemnt
```
pip install -r requirements.txt
cd inference_template
python manage.py migrate
```

# Implement Your Inference
in ```inference.views.inference```, your write your inference and return result

# Run Website
```
python manage.py runserver
```
- Open http://localhost:8000

# Create Super user
```
python manage.py createsuper
```
- username
- email
- password
- When you activate the website, you can log in to the backend using the following URL with your username and password.
- [http://localhost:8000/admin](http://localhost:8000/admin)

# Deployment
TBD

# Refernece
- [Django Document](https://docs.djangoproject.com/)
- [Bootstrap v5 Document (Chinese)](https://bootstrap5.hexschool.com/)
