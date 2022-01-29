# Menu Item: 
 - FastAPI
 - Uvicorn
 - Jinja2
 - Fastapi-users
 - Tortoise-orm
 - aerich

## Install and Run
```bash
pipenv install -r requirements.txt
pipenv shell uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
or 
```bash
cd fabulous
./run.sh
```

## Preparation
launch postgres database and pgadmin web server
```bash
cd utils
chmod +x *.sh
./container-up.sh
```