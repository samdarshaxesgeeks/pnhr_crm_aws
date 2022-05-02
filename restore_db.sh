#!/bin/bash

echo "==> Migrating to the db"
python manage.py makemigrations
python manage.py migrate

echo "==> Loading user fixtures..."
python manage.py loaddata fixtures/users.json

echo "==> Loading currencys fixtures..."
python manage.py loaddata fixtures/currencys.json

echo "==> Loading employees fixtures..."
python manage.py loaddata fixtures/employees.json

echo "==> Loading users fixtures..."
python manage.py loaddata fixtures/users.json

echo "==> Loading soliton users fixtures..."
python manage.py loaddata fixtures/soliton_users.json

echo "==> Loading departments..."
python manage.py loaddata fixtures/departments.json

echo "==> Loading positions..."
python manage.py loaddata fixtures/positions.json


echo "==> Loading teams..."
python manage.py loaddata fixtures/teams.json

echo "==> Loading organisation details..."
python manage.py loaddata fixtures/organisation_details.json

echo "==> Done!"
