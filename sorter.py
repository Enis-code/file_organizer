import os
import shutil
import json
from logger import logger

def load_config(config_path="config.json"):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Configuration file {config_path} not found.")
        return {}

def organize_directory(target_dir):
    if not os.path.isdir(target_dir):
        logger.error(f"Target directory {target_dir} does not exist.")
        return False
    
    config = load_config()
    ext_map = {ext: category for category, exts in config.items() for ext in exts}

    moved_count = 0
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            category = ext_map.get(ext, "Others")
            category_dir = os.path.join(target_dir, category)
            
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
            
            dest_path = os.path.join(category_dir, filename)
            shutil.move(file_path, dest_path)
            logger.info(f"Moved {filename} to {category}/")
            moved_count += 1
            
    logger.info(f"Organization complete. Moved {moved_count} files.")
    return True