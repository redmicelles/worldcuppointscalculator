""""
This module runs all setup
"""
from os import system

# Upgrade PIP
system("python.exe -m pip install --upgrade pip")

# Install Python Poetry Version 1.5.1
system("pip install poetry==1.5.1")

# Start Poetry Virtual Environment
# system("poetry shell")

# Install all dependencies using Poetry
system("poetry install")
