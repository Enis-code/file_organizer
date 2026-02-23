import argparse
import sys
from sorter import organize_directory

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer CLI")
    parser.add_argument("directory", help="The target directory to organize")
    
    args = parser.parse_args()
    
    success = organize_directory(args.directory)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()