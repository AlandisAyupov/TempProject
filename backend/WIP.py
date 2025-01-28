#Asks and downloads venv and requirements

import os
import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def ask_user(prompt):
    """Creates a popup to ask the user a yes/no question."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    return messagebox.askyesno("Confirmation", prompt)

def create_virtual_env(venv_dir="venv"):
    """Creates a virtual environment in the specified directory."""
    user_input = ask_user("Do you want to create a virtual environment?")
    if user_input:
        venv_path = Path(venv_dir)
        if venv_path.exists():
            print(f"Virtual environment already exists at {venv_dir}")
        else:
            print(f"Creating virtual environment at {venv_dir}...")
            subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
            print("Virtual environment created.")
    else:
        print("Skipping virtual environment creation.")

def install_requirements(requirements_file="requirements.txt", venv_dir="venv"):
    """Installs requirements into the specified virtual environment."""
    user_input = ask_user("Do you want to install the requirements from the file?")
    if user_input:
        venv_bin = Path(venv_dir) / ("Scripts" if os.name == "nt" else "bin")
        pip_path = venv_bin / "pip"

        if not pip_path.exists():
            raise FileNotFoundError(f"Pip not found in virtual environment {venv_dir}. Is the venv properly set up?")

        if not Path(requirements_file).exists():
            raise FileNotFoundError(f"Requirements file {requirements_file} not found.")

        print(f"Installing requirements from {requirements_file}...")
        subprocess.check_call([str(pip_path), "install", "-r", requirements_file])
        print("Requirements installed successfully.")
    else:
        print("Skipping requirements installation.")
    
create_virtual_env()
install_requirements()
