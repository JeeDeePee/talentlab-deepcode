# Heroku Release Phase Script
# https://devcenter.heroku.com/articles/release-phase
# https://devcenter.heroku.com/articles/pipelines#can-i-run-scripts-such-as-rake-db-migrate-when-promoting

# Run migration
python server/manage.py migrate --no-input

# create dummy data
python server/manage.py dummy_data

# clear cache
python server/manage.py clear_cache

# Run production checks
python server/manage.py check --deploy
