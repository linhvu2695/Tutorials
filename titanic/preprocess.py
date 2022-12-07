from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

def handleNull(df):
    df["embark"].fillna(df["embark"].mode()[0], inplace=True)
    df["age"].fillna(df["age"].mean(), inplace=True)

def dropColumns(df):
    df.drop(["cabin", "passengerid", "name", "ticket"], axis=1, inplace=True)

def encodeCategoricalColumns(df):
    # Pclass is ordinal: 1st class > 2nd class > 3rd class
    encoder = OrdinalEncoder()
    df[["pclass"]] = encoder.fit_transform(df[["pclass"]])

    encoder = OneHotEncoder(drop="first", sparse=False)
    df[encoder.get_feature_names(["is", "embarked_from"])] = encoder.fit_transform(df[["sex", "embark"]])

    df.drop(["sex", "embark"], axis=1, inplace=True)