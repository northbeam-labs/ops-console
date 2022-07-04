# ops-console

internal ops platform: react console, node api, fastapi metrics, infra

## architecture

- **`web/`** — react + ts ops console
- **`api/`** — node/express ops api
- **`metrics/`** — fastapi metrics service
- **`infra/`** — terraform + k8s

Each service is independently buildable; `docker-compose.yml` wires them
together for local dev.

## running locally

```
docker compose up --build
```

## layout

```
ops-console/
  web/
  api/
  metrics/
  infra/
  docker-compose.yml
  Makefile
```

