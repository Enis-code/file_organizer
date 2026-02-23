import os
import tempfile
import json
from sorter import organize_directory

def test_organize_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        config_data = {"Images": [".jpg"], "Documents": [".txt"]}
        with open("config.json", "w") as f:
            json.dump(config_data, f)
        
        open(os.path.join(temp_dir, "photo.jpg"), 'w').close()
        open(os.path.join(temp_dir, "notes.txt"), 'w').close()
        
        success = organize_directory(temp_dir)
        assert success is True
        
        assert os.path.exists(os.path.join(temp_dir, "Images", "photo.jpg"))
        assert os.path.exists(os.path.join(temp_dir, "Documents", "notes.txt"))
        
        if os.path.exists("config.json"):
            os.remove("config.json")
            