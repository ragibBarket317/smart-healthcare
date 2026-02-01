import json
import os

class DataLoader:
    def __init__(self, data_base_path= "data"):
        self.base_path = data_base_path

    def load(self, filename):
        with open(os.path.join(self.base_path, filename), 'r') as file:
            return json.load(file)
        
    def save(self, filename, data):
        with open(os.path.json(self.base_path, filename), 'w') as file:
            json.dump(data, file, indent=2)  
            