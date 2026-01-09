import os
from pathlib import Path

list_of_files = [
    "configs/config.yaml",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "notebooks/01_data_understanding.ipynb",
    "reports/data_quality/.gitkeep",
    "reports/drift_reports/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/db_injection.py",
    "src/components/data_ingestion.py",
    "src/pipeline/__init__.py",
    "requirements.txt",
    "setup.py",
    ".gitignore",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
            
print("MLOps Structure Created Successfully!")