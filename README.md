# FastFood API

A REST API for the [FastFood Web App](https://github.com/EdwinWalela/fastfood)

## Tech Stack

- Python (Django Rest Framework)
- Postgres (Database)
- Swagger (Documentation)

## Local Development

Clone repository

```bash
git clone https://github.com/EdwinWalela/fastfood-api
```

Create .env file

```bash
cp .sample.env .env
```

Start services

```bash
docker-compose up
```

Run migrations and create super user

```
docker exec -it bash <api-container-id>

python manage.py migrate 

python manage.py createsuperuser
```
