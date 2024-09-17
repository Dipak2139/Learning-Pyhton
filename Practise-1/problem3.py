import os

def print_directory_contents(path='/New Folder'):
    try:
        # Get the list of entries in the directory
        entries = os.listdir(path)
        
        # Print each entry
        for entry in entries:
            print(entry)
    
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory_path = '.'  # Current directory
print_directory_contents(directory_path)
