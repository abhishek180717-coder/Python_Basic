# Loan Prediction ML Mini Project:-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, confusion_matrix


# 1. Load Dataset:-
df = pd.read_csv("loan_prediction.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df["Loan_Status"].value_counts())


# 2. Data Cleaning:-
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = le.fit_transform(df[col])

# 3. EDA:-

# Income Distribution:-
plt.figure(figsize=(6,4))
plt.hist(df["ApplicantIncome"], bins=20)
plt.title("Applicant Income")
plt.show()

# Loan Amount by Education:-
plt.figure(figsize=(6,4))
sns.boxplot(x=df["Education"], y=df["LoanAmount"])
plt.title("Loan Amount by Education")
plt.show()

# Loan Status Count:-
plt.figure(figsize=(5,4))
sns.countplot(x=df["Loan_Status"])
plt.show()

# Property Area:-
plt.figure(figsize=(5,4))
sns.countplot(x=df["Property_Area"])
plt.show()

# Correlation Heatmap:-
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

# 4. Train Models:-
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(eval_metric="logloss")
}

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    print("\n", name)

    print("Accuracy :", accuracy_score(y_test, pred))
    print("Precision:", precision_score(y_test, pred))
    print("Recall   :", recall_score(y_test, pred))
    print("F1 Score :", f1_score(y_test, pred))

    print("Confusion Matrix")
    print(confusion_matrix(y_test, pred))

# 5. Feature Importance:-
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
).sort_values()

importance.plot(kind="barh", figsize=(8,5))
plt.title("Feature Importance")
plt.show()


# 6. Predict New Applicants:-
new_applicants = X.head(5)

prediction = rf.predict(new_applicants)

probability = rf.predict_proba(new_applicants)

print("\nPredictions")

for i in range(5):
    print("Applicant", i+1)
    print("Prediction:", prediction[i])
    print("Approval Probability:", round(probability[i][1],2))
    print("-------------------")