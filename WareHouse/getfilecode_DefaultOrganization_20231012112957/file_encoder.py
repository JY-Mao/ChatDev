'''
This file contains the FileEncoder class, which is responsible for encoding the files in the "test" directory.
'''
import os
class FileEncoder:
    def __init__(self, root):
        self.root = root
        self.file_tree = self.build_file_tree()
        self.file_counter = 1
    def build_file_tree(self):
        '''
        Builds the file tree structure for the files in the "test" directory.
        '''
        file_tree = {}
        for root, dirs, files in os.walk("test"):
            current_dir = file_tree
            for dir in root.split(os.path.sep):
                current_dir = current_dir.setdefault(dir, {})
            for file in files:
                current_dir[file] = None
        return file_tree
    def encode_files(self):
        '''
        Encodes the file tree structure by calling the encode_file_tree method.
        '''
        self.encode_file_tree(self.file_tree)
    def encode_file_tree(self, file_tree):
        '''
        Encodes the file tree structure recursively.
        '''
        for file, children in file_tree.items():
            if children is None:
                self.encode_file(file)
            else:
                self.encode_file_tree(children)
    def encode_file(self, file):
        '''
        Encodes a single file by renaming it with the encoded file number.
        '''
        # Generate the file number based on the file counter
        file_number = f"{self.file_counter:04}"
        self.file_counter += 1
        # Get the file path
        file_path = os.path.join("test", file)
        # Rename the file with the encoded file number
        encoded_file_name = f"{file_number}_{file}"
        encoded_file_path = os.path.join("test", encoded_file_name)
        os.rename(file_path, encoded_file_path)
        # Update the file tree with the encoded file name
        self.update_file_tree(file, encoded_file_name)
    def update_file_tree(self, old_file_name, new_file_name):
        '''
        Updates the file tree structure with the encoded file name.
        '''
        for root, dirs, files in os.walk("test"):
            for file in files:
                if file == old_file_name:
                    file_path = os.path.join(root, file)
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(file_path, new_file_path)
                    break