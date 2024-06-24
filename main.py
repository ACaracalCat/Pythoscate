import tkinter as tk
from tkinter import filedialog
import base64
import codecs
import time

print("Pythoscate Launched. Please Select a file.")

def file_select():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    return path

path = file_select()

if path:
    with open(path, 'r') as file:
        script_content = file.read()
    
    for i in range(10):
        base64_encoded = base64.b64encode(script_content.encode()).decode()
        rot13_encoded = codecs.encode(base64_encoded, 'rot_13')
        ascii85_encoded = base64.a85encode(rot13_encoded.encode()).decode()

        encoded_exec = (
            "import base64\n"
            "import codecs\n"
            f"exec(base64.b64decode(codecs.decode(base64.a85decode({repr(ascii85_encoded)}).decode(), 'rot_13')).decode())"
        )

        script_content = encoded_exec

        with open(path, 'w') as file:
            file.write(encoded_exec)

        print(f"Obfuscated {i+1} time(s)")

    print(f"Obfuscated {path}!")

else:
    print("No file selected...")

time.sleep(2.5)
exit()
