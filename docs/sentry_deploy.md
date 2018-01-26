
### Deploy Sentry with docker-compose

- `docker run --rm sentry config generate-secret-key` and Change SENTRY_SECRET_KEY in docker-compose
- `docker-compose up -d`
- `docker-compose exec sentry sentry upgrade` to setup database and create admin user
- `docker-compose restart`
- (Optional) `docker-compose exec sentry pip install sentry-slack`