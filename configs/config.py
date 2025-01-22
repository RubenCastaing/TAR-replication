import sys
import os

# Add the directory to sys.path
api_keys_dir = r'C:\Users\User\Desktop\Rubens_Stuff'
sys.path.append(api_keys_dir)

# Import the variable from API_keys.py
from API_keys import HF_API_key

TOKEN = os.environ.get(HF_API_key, "default_token")
CACHE_DIR = os.environ.get("cache_dir", "./cache")  # Default to a 'cache' folder in the current directory
HF_HOME = os.environ.get("HF_HOME", "./hf_home")  # Default to an 'hf_home' folder in the current directory
SAVE_MODELS_DIR = os.environ.get("SAVE_MODELS_DIR", "./saved_models")  # Default to a 'saved_models' folder in the current directory
USER = os.environ.get("RubenCastaing", "default_user")  # Default to 'default_user'
