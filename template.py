
import os
from pathlib import Path 

project_name = "app"

list_of_files = [
  f"{project_name}/__init__.py",
  f"{project_name}/backend/__init__.py",
  f"{project_name}/backend/api.py",
  f"{project_name}/common/__init__.py",
  f"{project_name}/common/logger.py",
  f"{project_name}/common/custom_exception.py",
  f"{project_name}/config/__init__.py",
  f"{project_name}/config/settings.py",
  f"{project_name}/core/__init__.py",
  f"{project_name}/core/ai_agent.py",
  f"{project_name}/frontend/__init__.py",
  f"{project_name}/frontend/ui.py",
  f"{project_name}/main.py",
  "custom_jenkins/Dockerfile",
  "requirements.txt",
  "setup.py",
  "Dockerfile",
  "Jenkinsfile",
  ".env"
  
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")
