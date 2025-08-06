import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_path_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path_wk_dir = os.path.abspath(working_directory)
    
    if abs_path_file.startswith(abs_path_wk_dir) == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if os.path.exists(abs_path_file) == False:
        return f'Error: File "{file_path}" not found.'
    
    if file_path.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python", abs_path_file]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_path_wk_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
