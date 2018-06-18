# TalentLab

Sources

* [Django](https://docs.djangoproject.com/en/2.0/)
* [Wagtail](http://docs.wagtail.io/)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [Vue-Apollo](https://github.com/Akryum/vue-apollo)
* [Vuetifyjs](https://vuetifyjs.com/en/getting-started/quick-start)

## Development

### Server

* [Install](https://docs.pipenv.org/#install-pipenv-today) pipenv
* Create virtualenv in install dependencies `pipenv --python 3.6 install --dev`
* Create PostgreSQL database & user
* [Install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) Heroku cli, run `heroku login` and `heroku git:remote -a caruhome`
* Create .env in `server` file with `SECRET_KEY` and `DATABASE_URL`
* Migrate databases: `pipenv run python manage.py migrate`
* Create super user: `pipenv run python manage.py createsuperuser`
* Run: `pipenv run python manage.py runserver`
* Dummy data: `pipenv run python manage.py dummy_data` (restart the development server afterwards)



#### Notes

* `DEBUG=True` enables the debug middleware http://docs.graphene-python.org/projects/django/en/latest/debug/


### Client

``` bash
# install dependencies
npm install --prefix client

# serve with hot reload at localhost:8080
npm run dev --prefix client

# build
npm run build --prefix client

# build for production with minification
export NODE_ENV=production && npm install --prefix client && npm run build --prefix client
```

After running `npm run dev` login to the Django admin view on the same domain as the webpack dev server is running.
Example: The client runs on localhost:8080 and Django on localhost:8000. 
This way you will have a session and a csrf cookie set and the apollo client will 
be able to make requests.

Production Build

## Urls

(trailing slashes are required)

* Admin interface: http://127.0.0.1:8000/guru/
* Cms interface: http://127.0.0.1:8000/cms/
* GraphQL Interface: http://localhost:8000/api/graphiql/

## Heroku

`heroku run python server/manage.py <command> --app <appname>`

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