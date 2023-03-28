import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

data = pd.read_csv("sensordata.csv", encoding='utf-8')

# Split your data into a training set and a test set
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)



# Preprocess your data by extracting the features and labels
X_train = train_data.drop(['label', 'koncentration'], axis=1)
y_train = train_data[['label', 'koncentration']]
X_test = test_data.drop(['label', 'koncentration'], axis=1)
y_test = test_data[['label', 'koncentration']]


mlb = MultiLabelBinarizer(sparse_output=True)
ytrain = mlb.fit_transform(y_train.values)
ytest = mlb.transform(y_test.values)

# Train a multilabel logistic regression classifier using OneVsRestClassifier
classifier = OneVsRestClassifier(LinearDiscriminantAnalysis())
classifier.fit(X_train, ytrain)

# Make predictions on the test set
y_pred = classifier.predict(X_test)


# Convert the binary predictions back to label format using inverse_transform
#ypred = mlb.inverse_transform(ytr)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(ytest, y_pred)

ypred = mlb.inverse_transform(y_pred)
print("Accuracy:", accuracy)

print(y_pred.shape)
print(ypred)









