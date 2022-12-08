# Initialize Docker MongoDB with CSV data

### Process
1. Run MongoDB in a container with pre-initialized db and collection
2. Import CSV data into the database

## 1. Run MongoDB image
- Create `./docker-entrypoint-initdb.d/init-mongo.js` to initiate authenticated database and user
```
db.createUser(
    {
        user: "root",
        pwd: "password",
        roles: [
            {
                role: "readWrite",
                db: "mnistdb"
            }
        ]
    }
)
db.createCollection("mnist")
```
- Write `docker-compose` file. Take note to set `MONGO_INITDB_DATABASE` and share volumes with your js script as well as your persistent volume
```
// docker-compose.yml
...
environment:
    - MONGO_INITDB_DATABASE=mnistdb
    volumes:
    - ./mongo-volume:/data/db
    - ./docker-entrypoint-initdb.d/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro
```
- Execute `docker-compose up -d` as normal

## 2. Import CSV data
- A `./mongo-volume` folder is created. Move our CSV files inside so that we can import them to our database
- Enter the container shell 
```
docker exec -it <container_name> sh
```
- Import data (from the shell) 
```
# mongoimport \
--db <db_name> \
--collection <collection_name> \
--type=csv \
--file="/data/db/mnist_train.csv" \
--headerline
```
*(`headerline` indicates that the first row is header instead of data)*

- `mongo` is deprecated in MongoDB. We enter the database in the container using `mongosh` instead
```
mongosh

test> show dbs;
# output
admin    100.00 KiB
config    72.00 KiB
local     72.00 KiB
mnistdb  132.70 MiB
```
