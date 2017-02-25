from __future__ import print_function
import json, os
from sklearn import datasets
from sklearn import svm
from time import sleep
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import classification_report

class TrainFile():
  def __init__(self):
    self.vectors = []
    self.classes = []
    self.word_names = []

  def generate_training_data(self, folder_name, file_name):
    input_file = os.path.join(folder_name, file_name)
    if not os.path.exists(input_file):
      print("The file doesn't exist", input_file)
      return
    file_data = open(input_file,"r").readlines()[0]
    companies = json.loads(file_data)['companies'];
    for company in companies:
      keys = company.keys()
      keys.sort()
      current_vector = []
      for key in keys:
        if key == 'document' or key == 'name':
          continue
        if key == 'name' and company['class'] == 0:
          self.word_names.append(company[key])
          continue
        if key == 'class':
          self.classes.append(company[key])
          continue
        current_vector.append(company[key])
      self.vectors.append(current_vector)

  def generate_training_data_for_folder(self, folder_name):
    if not os.path.exists(folder_name):
      print("Folder name doesn't exist!!!!")
      return
    files = os.listdir(folder_name)
    for file_name in files:
      self.generate_training_data(folder_name, file_name)

  def get_vector_and_classes(self):
    return (self.vectors, self.classes)

  def get_names(self):
    return self.word_names

if __name__ == "__main__":
  file_trainer = TrainFile()
  file_trainer.generate_training_data_for_folder('new_dict_files')
  a = file_trainer.get_vector_and_classes()
  #print(a[0])
  x= np.array(a[0])
  #print(a[1])
  count_1 = sum(a[1])
  print("Count 0: " + str(len(a[1])-count_1) + " Count 1 : " + str(count_1))
  # print("Names")
  # print(file_trainer.get_names())
  y = np.array(a[1])
  svmr_classifier=svm.SVC(gamma=0.001,C=100.0, kernel = 'rbf')
  # svml_classifier=svm.SVC(gamma=0.001,C=100.0, kernel = 'linear')
  # svmp_classifier=svm.SVC(gamma=0.001,C=100.0, kernel = 'poly')
  # svms_classifier=svm.SVC(gamma=0.001,C=100.0, kernel = 'sigmoid')
  dt_classifier = DecisionTreeClassifier(max_depth=None, min_samples_split=2,random_state=0)
  rf_classifier = RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
  logreg_classifier = LogisticRegression(C=1e5)

  k_fold = KFold(n_splits=10)
  precision, recall = 0,0
  for train, test in k_fold.split(x):
       y_pred = (svmr_classifier.fit(x[train], y[train])).predict(x[test])
       val = precision_recall_fscore_support(y[test], y_pred, average='macro')
       print(val)
       precision, recall = precision + val[0], recall + val[1]
  print("SVMR Classifier: ", precision/10, recall/10)

  #precision, recall = 0,0
  #for train, test in k_fold.split(x):
  #      y_pred = (svml_classifier.fit(x[train], y[train])).predict(x[test])
  #      val = precision_recall_fscore_support(y[test], y_pred, average='macro')
  #      print(val)
  #      precision, recall = precision + val[0], recall + val[1]
  #print("SVML Classifier: ",precision/10, recall/10)
  #
  #precision, recall = 0,0
  #for train, test in k_fold.split(x):
  #      y_pred = (svmp_classifier.fit(x[train], y[train])).predict(x[test])
  #      val = precision_recall_fscore_support(y[test], y_pred, average='macro')
  #      print(val)
  #      precision, recall = precision + val[0], recall + val[1]
  #print("SVMP Classifier: ",precision/10, recall/10)

  #precision, recall = 0,0
  #for train, test in k_fold.split(x):
  #      y_pred = (svms_classifier.fit(x[train], y[train])).predict(x[test])
  #      val = precision_recall_fscore_support(y[test], y_pred, average='macro')
  #      print(val)
  #      precision, recall = precision + val[0], recall + val[1]
  #print("SVMS Classifier: ",precision/10, recall/10)

  precision, recall = 0,0
  for train, test in k_fold.split(x):
        y_pred = (dt_classifier.fit(x[train], y[train])).predict(x[test])
        val = precision_recall_fscore_support(y[test], y_pred, average='macro')
        print(val)
        precision, recall = precision + val[0], recall + val[1]
  print("DT Classifier: ",precision/10, recall/10)

  precision, recall = 0,0
  for train, test in k_fold.split(x):
        y_pred = (rf_classifier.fit(x[train], y[train])).predict(x[test])
        val = precision_recall_fscore_support(y[test], y_pred, average='macro')
        print(val)
        precision, recall = precision + val[0], recall + val[1]
  print("RF Classifier: ",precision/10, recall/10)

  precision, recall = 0,0
  for train, test in k_fold.split(x):
        y_pred = (logreg_classifier.fit(x[train], y[train])).predict(x[test])
        val = precision_recall_fscore_support(y[test], y_pred, average='macro')
	    #print(classification_report(y[test], y_pred))
        print(val)
        precision, recall = precision + val[0], recall + val[1]
  print("LOG REG Classifier: ",precision/10, recall/10)
