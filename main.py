import tkinter as tk
from tkinter import filedialog
import base64
import codecs
import time
import re
import random
import string

print("Pythoscate Obfuscator Launched. Please Select a file.")

def file_select():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    return path

path = file_select()

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

if path:
    with open(path, 'r') as file:
        script_content = file.read()

    function_names = re.findall(r'\bdef (\w+)\(', script_content)
    rename_map = {name: random_string() for name in function_names}

    for original_name, new_name in rename_map.items():
        script_content = re.sub(rf'\b{original_name}\b', new_name, script_content)

    for i in range(10):
        reversed_content = script_content[::-1]
        base64_encoded = base64.b64encode(reversed_content.encode()).decode()
        rot13_encoded = codecs.encode(base64_encoded, 'rot_13')
        ascii85_encoded = base64.a85encode(rot13_encoded.encode()).decode()

        encoded_exec = (
            "import base64\n"
            "import codecs\n"
            f"exec((base64.b64decode(codecs.decode(base64.a85decode({repr(ascii85_encoded)}).decode(), 'rot_13')).decode())[::-1])"
        )

        script_content = encoded_exec

    with open(path, 'w') as file:
        file.write(encoded_exec)

    print(f"Obfuscated {path}!")

else:
    print("No file selected...")

time.sleep(2.5)
