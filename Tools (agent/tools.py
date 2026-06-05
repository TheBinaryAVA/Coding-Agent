import os
import subprocess

WORKSPACE = "workspace"

def read_file(path):
    full_path = os.path.join(WORKSPACE, path)
    with open(full_path, "r") as f:
        return f.read()

def write_file(path, content):
    full_path = os.path.join(WORKSPACE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w") as f:
        f.write(content)

    return f"written: {path}"

def run_code(command):
    result = subprocess.run(
        command,
        shell=True,
        cwd=WORKSPACE,
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr
