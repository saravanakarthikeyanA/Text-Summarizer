import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init.py",
    f"src/{project_name}/components/__init.py",
    f"src/{project_name}/utils/__init.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init.py",
    f"src/{project_name}/config/__init.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init.py",
    f"src/{project_name}/entity/__init.py",
    f"src/{project_name}/constants/__init.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfiles",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]


for path in list_of_files:
    filepath = Path(path)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath,'w')as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"File {filename}already exist")