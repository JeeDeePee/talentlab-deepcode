# TalentLab

Sources

* [Django](https://docs.djangoproject.com/en/2.0/)
* [Wagtail](http://docs.wagtail.io/)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [Vue-Apollo](https://github.com/Akryum/vue-apollo)
* [Vuetifyjs](https://vuetifyjs.com/en/getting-started/quick-start)

## Development

* Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Install [Docker](https://docs.docker.com/install/)
* Install [Docker-Compose](https://docs.docker.com/compose/install/)
* Clone source `git@github.com:720dreams/talentlab.git` ([How-To](https://help.github.com/articles/cloning-a-repository))
* Copy `env.exmaple` to `server/.env`
* Build and start containers (see sections below)

### (Re-)build containers

Creates the postgres and web container, restores a data dump and creates a user (email `admin`, password `getinckd`)

```
docker-compose build
docker-compose run foundation
```

### Start containers

Start postgres and web container

```
docker-compose up web
```

Websites runs under: http://127.0.0.1:8000/


### Misc

Create and apply migrations

```
docker-compose run migrations
```

Enter django shell

```
docker-compose run shell
```

Enter bash

```
docker-compose run bash
```

Pip install

```
docker-compose run pipenv_install
```

Run a django command

```
docker-compose run web pipenv run python server/manage.py <command> <args1>
```

Clean up containers
```
docker-compose stop
docker-compose rm -f
```

Catch log of a container

```
 docker logs <container id> -f
```

## Urls

(trailing slashes are required)

* Admin interface: http://127.0.0.1:8000/guru/
* Cms interface: http://127.0.0.1:8000/cms/
* GraphQL Interface: http://localhost:8000/api/graphiql/

## Heroku

**Important:** Add nodejs (top) and python buildpack

Run a command: `heroku run python server/manage.py <command> --app <appname>`

### Rollabck

After doing a rollback under https://data.heroku.com/

`heroku pg:info --app=<appname>`

Change DATABASE URL (e.g after a rollback)

`heroku pg:promote HEROKU_POSTGRESQL_PINK`

### Backup

`heroku pg:backups:capture --app <appname>`

`heroku pg:backups:url b001 --app <appname>`

## AWS

1. Create user with API Access and add `access key id` and `access key` to `.env` and set `USE_AWS=True`
2. Create S3 Bucket in location EU Ireland

Change bucket `Permissions` / `Bucket Policy`

```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<bucket-name>/*"
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "AWS": "<user arn>"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::<bucket-name>/*",
                "arn:aws:s3:::<bucket-name>"
            ]
        }
    ]
}

```