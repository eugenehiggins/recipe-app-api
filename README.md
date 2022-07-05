# recipe-app-api
recipe api app

docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"

docker-compose -f docker-compose-deploy.yml build app

docker-compose -f docker-compose-deploy.yml up --no-deps -d app

after updating requirements.txt:
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"
