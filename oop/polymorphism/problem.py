'''Create a FileHandler base class with methods read() and write(). 
Implement handlers for:

TextFileHandler (.txt)
JSONFileHandler (.json)
CSVFileHandler (.csv)

Each handler should read/write in its specific format. 
Create a function that processes any file type polymorphically.'''

class FileHandler:
    def read(self, file_path):
        pass

    def write(self, file_path, data):
        pass

class TextFileHandler(FileHandler):
    def read(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
        
    def write(self, file_path, data):
        with open(file_path, 'w') as f:
            f.write(data)
        
class JSONFileHandler(FileHandler):
    def read(self, file_path):
        import json
        with open(file_path, 'r') as f:
            return json.load(f)

    def write(self, file_path, data):
        import json
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

class CSVFileHandler(FileHandler):
    def read(self, file_path):
        import csv
        with open(file_path, 'r') as f:
            return list(csv.reader(f))
        
    def write(self, file_path, data):
        import csv
        with open(file_path, 'w', newline='') as f:
            csv.writer(f).writerows(data)

def process_file(handler, file_path, data):
    handler.write(file_path, data)     
    return handler.read(file_path)

txt = TextFileHandler()
jsonh = JSONFileHandler()
csvh = CSVFileHandler()

print(process_file(txt, "a.txt", "Hello"))  
print(process_file(jsonh, "a.json", {"x": 10}))
print(process_file(csvh, "a.csv", [["name", "age"], ["Priya", 22]]))
