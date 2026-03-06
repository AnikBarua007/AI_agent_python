
import os
import subprocess
import google.genai.types as types
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the Python file",
            )
        },
        required=["file_path"],
    ),
)
def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(
            command,
            cwd=working_directory_abs,
            capture_output=True,
            text=True,
            timeout=30,
            )
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if result.stdout=="" and result.stderr=="":
            return "No output produced"
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"