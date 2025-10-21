## Installation

> Note: These instructions are for deploying the UI

With the first install, it is `crucial` to set the secrets for the database.

```
helm upgrade --install boggled ./helm -n boggled --create-namespace
```

## Secrets

> The karns-online group access token in gitea is used here

You will need to create the secrets for the application to use.

Gitea Auth secret for pulling the container from the private registry

```
kubectl -n boggled \
  create secret docker-registry gitea-auth \
  --docker-server=https://gitea.pixelparasol.com \
  --docker-username=nathan \
  --docker-password=<redacted> \
  --docker-email=nathan@pixelparasol.com
```

## Build the image

### UI Instructions

```
cd ui

npm run build

DOCKER_REGISTRY="gitea.pixelparasol.com/nathan/boggled" && CI_COMMIT_SHORT_SHA=$(git rev-parse --short HEAD)

docker buildx build --no-cache -f Dockerfile . --platform linux/amd64 -t $DOCKER_REGISTRY/ui:latest -t $DOCKER_REGISTRY/ui:$CI_COMMIT_SHORT_SHA

docker login gitea.pixelparasol.com

docker push $DOCKER_REGISTRY/ui:$CI_COMMIT_SHORT_SHA; docker push $DOCKER_REGISTRY/ui:latest
```

### API Instructions

This application does not have an API

### Boggled Secrets

This application does not have secrets

### Database Secrets

This application does not have a databse

### Troubleshooting

You may find yourself in a state where you need to do secret checks to see how they render.
adding the `--dry-run=server` argument to your upgrade will render the secret checks.

```
helm upgrade boggled ./helm -n boggled --dry-run=server
```

## Helm Diff

Install the `helm-diff` plugin

```
helm plugin install https://github.com/databus23/helm-diff
```

view the diff if an upgrade were issued

> NOTE: this will show that secrets will be removed but thats not true

```
helm diff upgrade boggled ./helm -n boggled
```

## Deployment

Each component can be deployed individually by tag by specifiying it with `--set`

```
helm upgrade boggled ./helm -n boggled --set deploy.api.tag="v1.0.4"
helm upgrade boggled ./helm -n boggled --set deploy.db.tag="v1.0.4"
helm upgrade boggled ./helm -n boggled --set deploy.ui.tag="v1.0.4"
```
