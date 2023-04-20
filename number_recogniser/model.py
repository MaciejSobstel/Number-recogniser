import pickle
from number_recogniser import package_root
with open(package_root/"model.pkl", 'rb') as f:
    svm = pickle.load(f)


def prediction(example):
    predicted = svm.predict(example)
    print(predicted)
