import os

def write_file(working_directory, file_path, content):
    
    abs_path_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_wk_dir = os.path.abspath(working_directory)
    
    if abs_path_file.startswith(abs_path_wk_dir) == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        
        directory = os.path.dirname(abs_path_file)
        
        os.makedirs(directory, exist_ok=True)
        
        with open(abs_path_file, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    