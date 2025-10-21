# Docker Secret Pull Variables
DOCKER_USERNAME := nathan
DOCKER_EMAIL := nathan@pixelparasol.com

# Docker Image Variables
DOCKER_REGISTRY=gitea.pixelparasol.com/nathan
IMAGE_NAME := boggled
TAG := $(shell git rev-parse --short HEAD)
# TAG := $(GIT_HASH)
# TAG := latest

all: npm-build docker-build docker-login docker-push

npm-build:
	npm run build

docker-build:
	docker buildx build --no-cache -f Dockerfile . --platform linux/amd64 \
		-t $(DOCKER_REGISTRY)/$(IMAGE_NAME):$(TAG) \
		-t $(DOCKER_REGISTRY)/$(IMAGE_NAME):latest

docker-login:
	docker login gitea.pixelparasol.com

docker-push:
	docker push $(DOCKER_REGISTRY)/$(IMAGE_NAME):$(TAG)
	docker push $(DOCKER_REGISTRY)/$(IMAGE_NAME):latest
