import os
import subprocess
def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir,file_path))

        if os.path.commonpath([abs_working_dir,target_file]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if os.path.splitext(target_file)[-1] != '.py':
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        process = subprocess.run(command, text=True, capture_output=True, timeout=30)
        result=""
        if process.returncode != 0:
            result += f'Process exited with code "{process.returncode}"'
        if process.stdout == "" and process.stderr == "":
            result += f"No output produced"
        else:
            result += f"STDOUT: {process.stdout}\n"
            result += f"STDERR: {process.stderr}\n"
        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"
