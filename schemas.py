schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

schema_get_file_content = {
    "type": "function",
    "function":{
        "name": "get_file_content",
        "description": "List the content of the specifies file, path relative to the current working directory, providing content capped at a configurable limit",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to get the content from, relative to the working directory (default is the working directory itself)",
                }
            }
        }
    }
}
schema_run_python_file = {
    "type": "function",
    "function":{
        "name": "run_python_file",
        "description": "runs a python file locally, and returns the stdout, stderr and returncode",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the python file, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "description": "The list of arguments to be processed",
                    "items":{ "type": "string" }
                }
            }
        },
        "required":["file_path"]
    }
}
schema_write_file = {
    "type": "function",
    "function":{
        "name": "write_file",
        "description": "writes into a python file locally, and returns the length of content written",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the python file, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "content to be written in the specified file",
                }
            }
        },
        "required":["file_path"]
    }
}

