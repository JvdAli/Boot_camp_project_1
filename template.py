import os, sys
from pathlib import Path
import logging

#asking for project name from the user
while True:
    project_name = input("enter the project name: ")
    if project_name != "":       #if project name not entered then terminate the program
        break

#creating all necessary folders & files
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    #f"{project_name}/config/config.yaml",
    #f"{project_name}/config/schema.yaml",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/pipeline/__init__.py",		
    f"{project_name}/utils/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"config/config.yaml",
    f"config/schema.yaml",
    "schema.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "logs.py",
    "exception.py",
    "requirements.txt",
    "dvc.yaml"

]    

for filepath in list_of_files:
    filepath = Path(filepath) #backslash(\) is used in Windows, "Path" helps to resolve this conflict
    filedir,filename = os.path.split(filepath)  #this is used to split folder and file 

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)   #create folder ,if exists then donot create one

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # if file size is zero overwrite else skip
        with open(filepath, "w") as f:      # w for write
            pass
        #logging.info(f"Creating empty file:{filepath}")  # generating log message for files

    else:
        logging.info(f"{filename} already exists)")