#Source- http://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting
#example of svm model training on iris data
from sklearn import datasets
from sklearn import svm
from time import sleep

# loading data
iris=datasets.load_iris()
vectors=iris.data
classNames=iris.target

#training a SVM model on all but last 2 data points
classifier=svm.SVC(gamma=0.001,C=100.0)
classifier.fit(vectors[:-2],classNames[:-2])
print("classifier information=\n"+str(classifier))

#Predicted class of last two data points
for i in range(len(vectors[-2:])):
        predicted_class=classifier.predict(vectors[i]);
        ground_truth_class=classNames[i];
        temp_str="predicted class=%s \t ground truth class=%s"%(str(predicted_class[0]),str(ground_truth_class))
        print(temp_str)


"""        
Other classifiers that will be trained are :-
1. SVM - different kernels
2. Stochastic gradient descent
3. Nearest Neighbors
4. Gaussian Process classification
5. Decision Tree
6. Random forests 
7. Neural Network
"""

