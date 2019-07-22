from tkinter import *
from tkinter import ttk
from datetime import datetime
from ttkthemes import themed_tk as tk
import time, random

root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.title("Reaction Time")

content = ttk.Frame(root, padding=(3,3,12,12), width=500, height=100)
content.pack()

def click():    #begin program
    global start_time
    elapsed = str(round((time.time() - start_time), 3))+" seconds"
    result.set(elapsed)

result = StringVar()

def start(): #generates random countdown timer
    t = 3
    def countdown(num): #function to provide countdown effect
        start_var.set(num)
        if num >=1:
            num -= 1
            root.after(1000,lambda: countdown(num)) #call itself again until countdown reaches 0
        else:
            time.sleep(random.randint(2,6))
            start_var.set("GO!")
            global start_time
            start_time = time.time()
    countdown(t)

start_var = StringVar()

ttk.Button(content, text="Start", command=start, width=5).grid(column=1, row=1, sticky=W, padx= 30)
ttk.Label(content, text="Click on Go!").grid(column=2, row=1, sticky=S)
ttk.Button(content, text="Go", command=click, width=5).grid(column=2, row=2, sticky=(N,S))
ttk.Label(content, text="Result is: ").grid(column=3, row=2, sticky=S)
ttk.Label(content, textvariable=start_var).grid(column=1, row=2, sticky=(N,S))
ttk.Label(content, textvariable=result).grid(column=3, row=4, sticky=(N,S))

root.columnconfigure(0, weight=3)
root.rowconfigure(0, weight=3)
content.columnconfigure(1, weight=3, minsize=100)
content.columnconfigure(2, weight=0, minsize=100)
content.columnconfigure(3, weight=3, minsize=100)
content.rowconfigure(1, weight=3, minsize=100)
content.rowconfigure(2, weight=3, minsize=100)
content.rowconfigure(3, weight=3, minsize=100)

root.mainloop()