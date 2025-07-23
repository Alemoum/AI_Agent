import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_path_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_wk_dir = os.path.abspath(working_directory)
    
    if abs_path_file.startswith(abs_path_wk_dir) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isfile(abs_path_file) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        
        with open(abs_path_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
        if os.path.getsize(abs_path_file) > MAX_CHARS:
            return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_string

    except Exception as e:
        return f"Error: {e}"
