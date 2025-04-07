# src/auth.py

# Imports
import os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv("API")
WORKSPACE = os.getenv("WORKSPACE")
PROJECT = os.getenv("PROJECT")
EMAIL = os.getenv("EMAIL")

required_vars = {
    "API": API,
    "WORKSPACE": WORKSPACE,
    "PROJECT": PROJECT,
}