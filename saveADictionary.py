# Challenge
# Write a Python function to save a dictionary file 
# also
# Write a Python function to sort the words in a string 

import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(dict_to_save, file)
        
def load_dict(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)


dict = {1:"one", 2:"two", 3:"three"}

save_dict(dict, "pickleDict")

print(load_dict("pickleDict"))
