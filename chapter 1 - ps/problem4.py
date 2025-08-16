import os

def print_directory_contents(path='/temp python'):
    """
    Prints the contents of the specified directory.
    Defaults to the current working directory.
    """
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except OSError as e:
        print(f"Error accessing '{path}': {e}")

if __name__ == "__main__":
    # You can pass a path as an argument here, or leave it empty to use current dir
    print_directory_contents("/path/to/your/directory")
