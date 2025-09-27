import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับคำนวณตารางสูตรคูณ
error_count = 0  # ตัวนับจำนวนครั้งที่เกิดข้อผิดพลาด

def show_output():
    global error_count
    expr = number_input.get()
    try:
        # ประเมินนิพจน์ทางคณิตศาสตร์อย่างปลอดภัย
        result = eval(expr, {"__builtins__": None}, {})
        output_label.config(
            text=f"คำตอบ = {result}",
            bg=bg_color,
            font=("Arial", 14),
            relief="solid",
            bd=2,
            highlightbackground="#2196F3",
            highlightcolor="#2196F3",
            highlightthickness=2
        )
        output_label.pack_configure(ipadx=30, ipady=10)
    except Exception as e:
        error_count += 1
        if error_count >= 3:
            messagebox.showerror("ข้อผิดพลาด", "กูบอกให้ใส่ตัวเลขที่ถูกต้องแล้วนะ! ลองใหม่อีกครั้ง")
        else:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่สมการที่ถูกต้อง เช่น 1+1, 2*2, 3/3")
        return
           
# สร้างหน้าต่างหลักของโปรแกรม
window = tk.Tk()
window.title("คำนวณตารางสูตรคูณ")
window.minsize(width=400, height=400)
bg_color = "#F0F8FF"
window.configure(bg=bg_color)

def show_main_page():
    # ลบ widget เดิมทั้งหมด
    for widget in window.winfo_children():
        widget.destroy()
    # สร้าง UI หน้าแรกใหม่
    title_label = tk.Label(master=window, text="กรุณาใส่สมการที่ต้องการคำนวณ", font=("Arial", 10, "bold"), bg=bg_color)
    title_label.pack(pady=20)

    global number_input, output_label
    number_input = tk.Entry(master=window, width=25, bg="#DCDCDC", font=("Arial", 16))
    number_input.pack(pady=5)

    button_frame = tk.Frame(master=window, bg=bg_color)
    button_frame.pack(pady=15, fill="x")

    go_button = tk.Button(master=button_frame, text="คำนวณ", command=show_output, bg="#2196F3", fg="white", width=10, height=2, font=("Arial", 11))
    go_button.pack(side="left", padx=(40, 0), pady=(20), expand=True)

    back_button = tk.Button(master=button_frame, text="ย้อนกลับ", command=show_main_page, bg="#FF7043", fg="white", width=10, height=2, font=("Arial", 11))
    back_button.pack(side="right", padx=(0, 40), pady=(20), expand=True)

    output_label = tk.Label(master=window, text="", font=("Arial", 10))
    output_label.pack(pady=20)

# เรียกหน้าแรกตอนเริ่มโปรแกรม
show_main_page()

window.mainloop()
