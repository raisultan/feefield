setup:
	docker-compose build
	docker-compose run --rm server sh -c "python manage.py migrate"
	docker-compose run --rm server sh -c "python manage.py collectstatic"
	docker-compose stop

up:
	docker-compose up -d

stop:
	docker-compose stop

build:
	docker-compose build

down:
	docker-compose down -v

createsuperuser:
	docker-compose run --rm server sh -c "python manage.py createsuperuser"
