import os

def get_files_info(working_directory, directory="."):
    
    abs_path_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_path_wk_dir = os.path.abspath(working_directory)
    
    if abs_path_dir.startswith(abs_path_wk_dir) == False:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if os.path.isdir(abs_path_dir) == False:
        print(f'Error: "{directory}" is not a directory')
        
    list_of_contents = os.listdir(abs_path_dir)
    for content in list_of_contents:
        abs_path_content = os.path.abspath(os.path.join(abs_path_dir, content))
        print(f"- {content}: file_size={os.path.getsize(abs_path_content)}, is_dir={os.path.isdir(abs_path_content)}")
    
