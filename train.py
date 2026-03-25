from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(df):
    features = ['field_goals', 'free_shots', 'three_point_goals']
    
    X = df[features]
    y = df['playoff_qualified']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "outputs/model.pkl")

    return model, X_test, y_test
