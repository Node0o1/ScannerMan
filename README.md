# ScannerMan
**Simple Domain Reconnaissance Scanner**
Type: Terminal Application

### Types of Scans currently supported
- Sub Domain
- Filepath
- Port

#### Description
> Very basic menu-driven, multi-threaded scanner tool written in Python and easy to use. Incorporates the use of a dictionary for path scans using the requests library and a range based port scan using Python sockets.
> Works on linux and Windows operating systems. 
> Many like it exist, but I wanted to build my own tool which offers ease of use and high efficiency. I may add more capabiltiy such as more scan types and CLI -tag options for single line use in the command line environment for more advanced users.

### A few things to note:
- Python 3.11+ is required to run
- Pip must be installed and Python should be added to Path

## **Instructions:**
#### **Download**
- Using git
  ```console
  git clone https://github.com/Node0o1/ScannerMan.git
  ```

#### **setup**
- after downloading, use the CLI to navigate to the directory containing the requirements.txt file and run the following command:
  
  ```console
  python -m pip install requirements.txt
  ```
  or
  
  ```console
  python3 -m pip install requirements.txt
  ```
  depending on your environment.

#### **Run**
  - From within the ScannerMan directory using CLI
    ```console
    python main.py
    ```
