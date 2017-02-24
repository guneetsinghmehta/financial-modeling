from __future__ import print_function
import json, os

class TrainFile():
  def __init__(self):
    self.vectors = []
    self.classes = []

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
        if key == 'name' or key == 'document':
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

if __name__ == "__main__":
  file_trainer = TrainFile()
  file_trainer.generate_training_data_for_folder('dictionary_files')
  a = file_trainer.get_vector_and_classes()
  print("Vectors")
  print(a[0])
  print("Classes")
  print(a[1])
  
