COMPOSE_FILE=docker-compose.yml

up:
	docker-compose -f $(COMPOSE_FILE) up -d

down:
	docker-compose -f $(COMPOSE_FILE) down

build:
	docker-compose -f $(COMPOSE_FILE) build

logs:
	docker-compose -f $(COMPOSE_FILE) logs

shell:
	docker-compose -f $(COMPOSE_FILE) exec web /bin/bash

stop:
	docker-compose -f $(COMPOSE_FILE) stop

clean-images:
	docker-compose -f $(COMPOSE_FILE) down --rmi all

clean-volumes:
	docker-compose -f $(COMPOSE_FILE) down -v

.PHONY: up down build logs shell stop clean-images clean-volumes