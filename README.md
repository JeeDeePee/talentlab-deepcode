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

#### Local setup

username = talentlab
email = talentlab@talentlab.ch
password = test

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

# Urls

(trailing slashes are required)

* Admin interface: http://127.0.0.1:8000/guru/
* Cms interface: http://127.0.0.1:8000/cms/
* GraphQL Interface: http://localhost:8000/api/graphiql/

# Heroku

`heroku run python server/manage.py <command> --app <appname>`

## Rollabck

After doing a rollback under https://data.heroku.com/

`heroku pg:info --app=<appname>`

Change DATABASE URL (e.g after a rollback)

`heroku pg:promote HEROKU_POSTGRESQL_PINK`

## Backup

`heroku pg:backups:capture --app <appname>`

`heroku pg:backups:url b001 --app <appname>`
