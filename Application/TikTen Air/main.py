"""
MIT License

Copyright (c) 2023 uǝ⊥ʞı⊥

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Software information:
background-color: #120248;
text-color: #657beb;
"""
# Import library
from tkinter import *
import webview

def Internet_connected():
    # Create values
    root = Tk()
    webview.create_window('TikTen Air', 'https://www.tiktenair.ir')
    webview.start()
    # Root options
    root.geometry("800x500")
def Internet_not_connected():
    root = Tk()
    icon_img = PhotoImage(file=r"Files\Images\Server images\server 7.png")
    Label(root, text="Interbet connection lost!", bg="white", fg="black", font=("", 15)).place(relx=0.15, rely=0.2)
    Label(root, text="Please Check Your Internet", bg="white", fg="black", font=("", 12)).place(relx=0.18, rely=0.30)
    Label(root, text="Connection And Try Again", bg="white", fg="black", font=("", 12)).place(relx=0.18, rely=0.4)
    Label(root, text="Later.", bg="white", fg="black", font=("", 12)).place(relx=0.40, rely=0.48)
    root.title("Internet connection lost!")
    root.iconphoto(False, icon_img)
    root.resizable(False,False)
    root.geometry("300x300")
    root.config(bg="white")
    root.mainloop()

import requests
try:
    response = requests.get("https://www.tiktenair.ir/", timeout=1)
    Internet_connected()
except requests.ConnectionError:
    Internet_not_connected()