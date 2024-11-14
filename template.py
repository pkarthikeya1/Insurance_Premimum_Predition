import os
from pathlib import Path

list_of_files= [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/pipelines/__init__.py",
    f"src/logging.py",
    f"src/custom_exception.py",
    f"notebooks/research.ipynb",
    f"requirements.txt",
    ".gitignore"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    try:
        if  file_dir !="":
            os.makedirs(file_dir, exist_ok=True)
    except:
        raise Exception
    
    try:
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path)== 0):
            with open(file_path, "w") as file:
                pass
    except:
        raise Exception