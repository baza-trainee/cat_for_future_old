pip install -r ./requirements/local.txt gunicorn collectfast django-anymail boto3
python manage.py migrate
python manage.py collectstatic
