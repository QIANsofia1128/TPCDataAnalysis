import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("/Users/qianqian/decisionTree_data.csv")

X = df.iloc[:, 1:5]
y = df.iloc[:, 0] 

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, test_size=0.2)

print("Xtrain size:", X_train.shape)
print("Xtest size:", X_test.shape)
print("ytrain size:", y_train.shape)
print("ytest size:", y_test.shape)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)
print(classification_report(y_test, y_pred))
print(dtc.feature_importances_)
features = pd.DataFrame(dtc.feature_importances_, index=X.columns)
print(features.head())
