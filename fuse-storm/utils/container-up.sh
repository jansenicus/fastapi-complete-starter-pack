#!/bin/sh
clear
export POSTGRES_PASSWORD=Xr1tozS4lv@t0rMund!
export PGADMIN_DEFAULT_PASSWORD=Xr1stozS4lv@t0rMund!
export ADMIN_PORT=5050
export PGADMIN_DEFAULT_EMAIL=angelis@sanctus.net
docker pull postgres:latest
docker pull dpage/pgadmin4:latest
docker run -p 5432:5432 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d postgres
docker run -p $ADMIN_PORT:80  -e "PGADMIN_DEFAULT_EMAIL=$PGADMIN_DEFAULT_EMAIL" -e "PGADMIN_DEFAULT_PASSWORD=$PGADMIN_DEFAULT_PASSWORD"  -d dpage/pgadmin4
export POSTGRESQL_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep postgres | awk '{print $1}'))
clear
tput setaf 51; echo ---------------------------------------------------------
echo POSTGRESQL DATABASE SERVER
echo Connection String
echo postgresl://$POSTGRESQL_IP:5432
tput setaf 3; echo POSTGRES_USERNAME=postgres
tput setaf 2; echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD
tput setaf 51; echo ---------------------------------------------------------
export ADMIN_DOMAIN=localhost
echo URL PG ADMIN:
echo http://$ADMIN_DOMAIN:$ADMIN_PORT
tput setaf 3; echo PGADMIN_DEFAULT_EMAIL: $PGADMIN_DEFAULT_EMAIL
tput setaf 2; echo PGADMIN_DEFAULT_PASSWORD = $PGADMIN_DEFAULT_PASSWORD
# ---------------------------------------
tput setaf 6;
if [[ "$OSTYPE" == "darwin"* ]]; 
then
    echo $PGADMIN_DEFAULT_PASSWORD | pbcopy
    echo 'password copied to clipboard'
fi
# ---------------------------------------
tput setaf 0;
./waiting-for.sh $ADMIN_DOMAIN:$ADMIN_PORT -q --timeout=0 -q --strict -- tput setaf 6; echo "PG ADMIN is ready..."
open "http://$ADMIN_DOMAIN:$ADMIN_PORT"
echo "try refreshing browser if not shown..."
echo ---------------------------------------------------------
