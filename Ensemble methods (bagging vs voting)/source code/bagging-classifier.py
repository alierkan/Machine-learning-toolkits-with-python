from sklearn import datasets
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score

data = datasets.load_digits()

X_data = data.images   # load X_data
y_data = data.target   # load y_data

X_data = X_data.reshape(X_data.shape[0], X_data.shape[1] * X_data.shape[2])    # flatten X_data
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size = 0.2, random_state = 7)    # split data into train & test set

bag_clf = BaggingClassifier(base_estimator = SVC(), n_estimators = 100, max_samples = 0.5, max_features = 1.0, random_state = 5)    # create a bagging classifier
bag_clf.fit(X_train, y_train)

y_pred = bag_clf.predict(X_test)
print(accuracy_score(y_pred, y_test))