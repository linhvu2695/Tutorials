# Initialize Docker Postgresql DB with CSV data

### Process
1. Build Postgresql image with pre-built schema
2. Run Postgresql in a container
3. Import the CSV data into database

## 1. Build Postgresql image
- Create schema using a `.sql` file
```
// setup.sql
CREATE TABLE passengers (
    PassengerId INTEGER NOT NULL,
    ...
)
```
- In the `Dockerfile`, place the `setup.sql` inside `/docker-entrypoint-initdb.d` folder to create schema in the initialization phase
```
// Dockerfile
FROM postgres:alpine
COPY *.sql /docker-entrypoint-initdb.d/
ADD setup.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
EXPOSE 5432
```
- Build the image using Dockerfile
```
docker build -t pg_titanic:latest .
```

## 2. Run Postgresql in a container
- Use a `docker-compose.yml` to run the docker image
```
docker-compose up -d
```
- (Optional) Run using `docker run`
```
docker run \
--name titanic_db \
-v ${PWD}/pgdata:/var/lib/postgresql/data \
-e POSTGRES_USER=root \
-e POSTGRES_PASSWORD=password \
-e POSTGRES_DB=titanic \
-p 5432:5432 \
pg_titanic:latest
```
- A `/pgdata` is created at `~/.../titanic/`. Place the CSV file inside `/pgdata` folder and it will be reflected in `/var/lib/postgresql/data`
- The `/pgdata` will persist even after the docker instance is stopped. If you want to remove it, add `--rm` in the docker run command. Remember to remove it if you want to make changes and rebuild the image.

## 3. Import CSV to database
- Start `psql` client on Dokcer database (`-d` to use database)
```
docker exec -it titanic_db psql -d titanic
```
- In `#titanic` database: import CSV file to database
```
\copy passengers FROM 'var/lib/postgresql/data/Titanic-Dataset.csv' DELIMITER ',' CSV HEADER;
```