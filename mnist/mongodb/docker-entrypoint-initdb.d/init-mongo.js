print("Start ####################################")
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