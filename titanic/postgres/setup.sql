CREATE TABLE passengers (
    PassengerId INTEGER NOT NULL,
    Survived BOOLEAN NOT NULL,
    Pclass INTEGER,
    Name TEXT,
    Sex TEXT,
    Age NUMERIC,
    SibSp INTEGER,
    Parch INTEGER,
    Ticket TEXT,
    Fare NUMERIC,
    Cabin TEXT,
    Embark TEXT,
    PRIMARY KEY (PassengerId)
);