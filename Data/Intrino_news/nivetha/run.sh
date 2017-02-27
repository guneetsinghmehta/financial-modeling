rm -rf new_dict_files/*
rm -rf classifier
python feature_extraction_from_document.py
python train_file_splitter.py
python classification_training.py
