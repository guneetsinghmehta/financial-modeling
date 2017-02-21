#Source - http://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting
from sklearn import datasets
from time import sleep
iris=datasets.load_iris()

#data can be a collection of n dimensional vector
vectors=iris.data
print("************vectors***********")
sleep(2)
print(vectors)

#target is the corresponding class of vector
classNames=iris.target
print("************class values***********")
sleep(2)
print(classNames)

#printing description of dataset
print("************Description of dataset***********\n")
sleep(2)
print(iris.DESCR)


