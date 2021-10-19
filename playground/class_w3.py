import os

class FileReader:

    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            os.path.exists(self.path)
            with open(self.path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

