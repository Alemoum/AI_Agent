import os

def get_files_info(working_directory, directory="."):
    
    abs_path_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_path_wk_dir = os.path.abspath(working_directory)
    
    if abs_path_dir.startswith(abs_path_wk_dir) == False:
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(abs_path_dir) == False:
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        for filename in os.listdir(abs_path_dir):
            filepath = os.path.join(abs_path_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
