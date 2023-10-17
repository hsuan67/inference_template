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
