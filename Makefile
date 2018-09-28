#start docker container
start:
	docker-compose up -d

#stop docker container
stop:
	docker-compose stop

#docker logs
logs:
	docker-compose logs

#django makemigrations
makemigrations:
	docker-compose run --rm web python manage.py makemigrations

#django migrate
migrate:
	docker-compose run --rm web python manage.py migrate

#psql
psql:
	docker exec -it lily_db_1 psql -U postgres
