import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.config(text=f"คุณได้ใส่ข้อมูล: {text}")
# Create the main window
    

Windows = tk.Tk()
Windows.title("Calculator")
Windows.minsize(width=400, height=400)

title_label = tk.Label (master=Windows, text="กรุณาใส่ข้อมูลของคุณ", font=("Arial", 10))
title_label.pack()

text_input = tk.Entry(master=Windows, width=30)
text_input.pack()

ok_button = tk.Button(master=Windows, text="ตกลง", command=set_message)
ok_button.pack()



Windows.mainloop()

