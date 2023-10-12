# File Numbering Software User Manual

## Introduction

The File Numbering Software is a Python-based application that allows you to encode files in the "test" directory with a unique file number. The encoded file number includes the file tree structure, file serial number, and file version number.

This user manual provides detailed instructions on how to install the software, how to use it, and its main functions.

## Installation

To install the File Numbering Software, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone or download the software code from the repository: [https://github.com/ChatDev/](https://github.com/ChatDev/)

3. Open a terminal or command prompt and navigate to the directory where you downloaded the software code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv env
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows:

     ```
     env\Scripts\activate
     ```

   - macOS/Linux:

     ```
     source env/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you are ready to use the File Numbering Software.

## Usage

To use the File Numbering Software, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the software code.

2. Activate the virtual environment (if you created one) by running the appropriate command.

3. Run the main.py file by executing the following command:

   ```
   python main.py
   ```

4. The software will launch a graphical user interface (GUI) window.

5. The software will automatically encode the files in the "test" directory. The encoded files will be renamed with a unique file number based on the file tree structure, file serial number, and file version number.

6. Once the encoding process is complete, you can find the encoded files in the "test" directory.

## Main Functions

The File Numbering Software provides the following main functions:

1. **Build File Tree Structure**: This function builds the file tree structure for the files in the "test" directory. The file tree structure represents the hierarchical organization of the files.

2. **Encode Files**: This function encodes the file tree structure by renaming the files with a unique file number. The file number includes the file tree structure, file serial number, and file version number.

3. **Update File Tree**: This function updates the file tree structure with the encoded file names.

## Conclusion

Congratulations! You have successfully installed and used the File Numbering Software. You can now easily encode files in the "test" directory with a unique file number. If you have any questions or need further assistance, please refer to the documentation or contact our support team.

Happy file encoding!