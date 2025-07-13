import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import shap

df = pd.read_csv("/Users/qianqian/decisionTree_data_encoding.csv")

X = df.iloc[:, 1:13]
y = df.iloc[:, 0] 

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, test_size=0.2)
print("Xtrain size:", X_train.shape)
print("Xtest size:", X_test.shape)
print("ytrain size:", y_train.shape)
print("ytest size:", y_test.shape)

dtc = RandomForestClassifier(n_estimators=100, random_state=42)
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)
print(classification_report(y_test, y_pred))
print(dtc.feature_importances_)
features = pd.DataFrame(dtc.feature_importances_, index=X.columns)
print(features)


# Create SHAP explainer
explainer = shap.TreeExplainer(dtc)

# Get SHAP values with column-aware input
shap_values = explainer.shap_values(X_test)
print(shap_values.shape)

# Print shape of SHAP values for class 1 (responders)
print("SHAP values shape:", shap_values[:,:,1].shape)  

# Generate dependence plot
shap.summary_plot(shap_values[:,:,1], X_test)

