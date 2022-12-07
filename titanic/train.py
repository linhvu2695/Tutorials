import psycopg2, pickle, logging
import pandas as pd
import schema, preprocess

logging.basicConfig(level=logging.INFO, filename="log/train.log", format='%(asctime)s - %(message)s')

# connect to the db
conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "titanic",
    user = "root",
    password = "password")
logging.info("Connect successfully!")

df = pd.read_sql("SELECT * FROM %s" %schema.TABLE_NAME, conn)
# preprocess data
preprocess.handleNull(df)
preprocess.dropColumns(df)
preprocess.encodeCategoricalColumns(df)

# training
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x, y = df.drop("survived", axis=1), df["survived"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

logging.info("Accuracy score: %f" %accuracy_score(y_true=y_test, y_pred=model.predict(x_test)))

# save model
pickle.dump(model, open("model/logistic_regression.pkl", "wb"))