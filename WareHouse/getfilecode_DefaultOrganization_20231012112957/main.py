'''
This is the main file of the file numbering software. It contains the main function that is responsible for running the software.
'''
import os
import tkinter as tk
from file_encoder import FileEncoder
def main():
    root = tk.Tk()
    app = FileEncoder(root)
    app.encode_files()  # Call the encode_files method to start encoding the files
    root.mainloop()
if __name__ == "__main__":
    main()