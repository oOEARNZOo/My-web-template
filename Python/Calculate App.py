import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับคำนวณตารางสูตรคูณ
def show_output():
    expr = number_input.get()
    try:
        # ประเมินนิพจน์ทางคณิตศาสตร์อย่างปลอดภัย
        result = eval(expr, {"__builtins__": None}, {})
        output_label.config(text=f"{expr} = {result}", font=("Arial", 14))
    except Exception:
        output_label.config(text="กรุณาใส่สมการที่ถูกต้อง เช่น 1+1, 2*2, 3/3", font=("Arial", 12))

# หน้าต้างหลักของโปรแกรม
window = tk.Tk()
window.title("คำนวณตารางสูตรคูณ")
window.minsize(width=400, height=400)
bg_color = "#F0F8FF"
window.configure(bg=bg_color)

title_label = tk.Label(master=window, text="กรุณาใส่ตัวเลขที่ต้องการคำนวณ", font=("Arial", 10, "bold"), bg=bg_color)
title_label.pack(pady=20)

number_input = tk.Entry(master=window, width=30)
number_input.pack()

go_button = tk.Button(master=window, text="คำนวณ",
                      command=show_output, width=10, height=2, font=("Arial", 10))
go_button.pack(pady=10)

output_label = tk.Label(master=window, text="", font=("Arial", 10))
output_label.pack(pady=20)


window.mainloop()