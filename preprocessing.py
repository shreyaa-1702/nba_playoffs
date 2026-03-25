import pandas as pd

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Drop missing values
    df = df.dropna()

    # Create target
    df['playoff_qualified'] = (df['rank'] <= 8).astype(int)

    # Encode categorical
    df = pd.get_dummies(df, columns=['position'], drop_first=True)

    return df
