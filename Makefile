.PHONY: help
.DEFAULT_GOAL := help

COMPOSE_FILE_OPT = -f ./docker/docker-compose.yml
DOCKER_COMPOSE_CMD = docker compose $(COMPOSE_FILE_OPT)

# Load .env file if exists
ifneq ($(wildcard .env),)
include .env
else
warning_msg:
$(warning There's no docker/.env file, please run make cp-env)
endif

export PYTHONPATH := "/code/:${PYTHONPATH}"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build backend image
	$(call log, Building backend image (using host SSH keys)...)
	DOCKER_BUILDKIT=1 $(DOCKER_COMPOSE_CMD) build

up: ## Start services
	$(call log, Starting services in detached mode...)
	$(DOCKER_COMPOSE_CMD) run -e OPENAI_API_KEY="${OPENAI_API_KEY}"  backend /bin/bash 