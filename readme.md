pull docker image bitnami/airflow2.3.4
use docker-compose.yml from my repository, insert your fernet and secret key in yml file
run airflow from docker by command docker compose up -d
Check that volumes has been connected and folder dags created
Once the containers are running, connect to db with admin tool and create under the running Postgres db from container a new DB with name test
Log in into the airflow, go to Admin > connections > and create new connection (
Connection Id >> my_db
Connection type >> Postgres
Host >> postgresql
Schema >> test
Login >> bn_airflow
Password >> bitnami1
Port >> 5432 )

Run the Dags. For the first run the table "sold" will be created. For another runs of dags
you can change the sql statement in dag_2 to avoid errors
