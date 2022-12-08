import pymongo
import numpy as np
import tensorflow as tf
import logging, pickle, time
import schema, src.preprocess as preprocess

def main():
    logfile = "log/train.log"
    logging.basicConfig(level=logging.INFO, filename=logfile, format="%(asctime)s - %(message)s")

    # Connect to MongoDB
    try:    
        client = pymongo.MongoClient("mongodb://localhost:27017/")
    except:
        logging.error("Fail to connect to MongoDB!")
        return
    logging.info("Connect successfully!")
    db = client[schema.DATABASE]
    collection = db[schema.COLLECTION]
    cursor = collection.find({})

    # Process data from MongoDB
    logging.info("Start preprocess data")
    start = time.time()
    X = np.zeros(shape=(schema.TRAIN_NUM,) + schema.INPUT_SHAPE)
    y = np.zeros(shape=(schema.TRAIN_NUM, 1))
    i = 0
    for doc in cursor:
        X[i] = preprocess.convertImage(doc)
        y[i] = doc["label"]
        print("Process image_%d completed" %i)
        i += 1
    logging.info("Data preprocessing completed after %.2f s" %(time.time() - start))

    # Modelling & Training
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=schema.INPUT_SHAPE),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation="softmax")
        ]
    )
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
    model.compile(
        optimizer="adam",
        loss=loss_fn,
        metrics=["accuracy"]
    )
    logging.info("Start training")
    results = model.fit(X, y, epochs=10)
    logging.info("Training accuracy: %.4f" %results.history["accuracy"][-1])
    pickle.dump(model, open("model/basicCNN.pkl", "wb"))

if __name__ == "__main__":
    main()