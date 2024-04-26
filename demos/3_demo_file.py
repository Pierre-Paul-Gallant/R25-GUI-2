from tkinter import filedialog
import json

with filedialog.askopenfile() as f_lu :
    text = f_lu.read()
    data = json.loads(text)

print(data)