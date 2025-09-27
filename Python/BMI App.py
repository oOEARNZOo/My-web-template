import tkinter as tk
# ฟังก์ชันสำหรับคำนวณค่า BMI
# ฟังก์ชันนี้จะคำนวณค่า BMI ตามน้ำหนัก ส่วนสูง และเพศที่ระบุ
def calculate_bmi(weight, height_cm, gender):
    weight = float(weight)
    height_cm = float(height_cm)
    if not weight or not height_cm:
        result_label.config(text="กรุณากรอกน้ำหนักและส่วนสูงให้ครบ")
        return

    if height_cm <= 0 or weight <= 0:
        raise ValueError("น้ำหนักและส่วนสูงต้องมากกว่า 0")
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi


def show_bmi_result(weight, height_cm):
    gender = gender_var.get()
    try:
        bmi = calculate_bmi(weight, height_cm, gender)
        result_text = f"ค่า BMI ของคุณคือ: {bmi:.2f}\n"
        if gender == "ชาย":
            if bmi < 18.5:
                result_text += "อยู่ในเกณฑ์: ผอม"
            elif bmi < 24.9:
                result_text += "อยู่ในเกณฑ์: ปกติ"
            elif bmi < 29.9:
                result_text += "อยู่ในเกณฑ์: น้ำหนักเกิน"
            else:
                result_text += "อยู่ในเกณฑ์: อ้วน"
        elif gender == "หญิง":
            if bmi < 18.0:
                result_text += "อยู่ในเกณฑ์: ผอม"
            elif bmi < 23.9:
                result_text += "อยู่ในเกณฑ์: ปกติ"
            elif bmi < 28.9:
                result_text += "อยู่ในเกณฑ์: น้ำหนักเกิน"
            else:
                result_text += "อยู่ในเกณฑ์: อ้วน"
        else:
            result_text += "อยู่ในเกณฑ์: ไม่สามารถประเมินผลได้"
    except Exception as e:
        result_text = f"เกิดข้อผิดพลาด: {e}"
    result_label.config(text=result_text)

# สร้างหน้าต่างหลักของโปรแกรม
window = tk.Tk()
window.title("คำนวณค่า BMI")
window.minsize(width=400, height=400)

def show_weight_height_page():
    for widget in window.winfo_children():
        widget.destroy()
    tk.Label(window, text="กรุณาใส่น้ำหนัก (Kg):", font=("Arial", 12)).pack(pady=10)
    weight_entry = tk.Entry(window)
    weight_entry.pack()
    tk.Label(window, text="กรุณาใส่ส่วนสูง (Cm):", font=("Arial", 12)).pack(pady=10)
    height_entry = tk.Entry(window)
    height_entry.pack()
    global result_label
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)
    def on_calculate():
        weight = weight_entry.get()
        height = height_entry.get()
        show_bmi_result(weight, height)
        
    tk.Button(window, text="คำนวณ", command=on_calculate).pack(pady=20)

def on_gender_submit():
    show_weight_height_page()

title_label = tk.Label(master=window, text="กรุณาใส่ข้อมูลของคุณ", font=("Arial", 10))
title_label.pack(pady=10)

tk.Label(window, text="เพศ:").pack()
gender_var = tk.StringVar()
tk.Radiobutton(window, text="ชาย", variable=gender_var, value="ชาย").pack()
tk.Radiobutton(window, text="หญิง", variable=gender_var, value="หญิง").pack()
tk.Button(window, text="ตกลง", command=on_gender_submit).pack(pady=20)

window.mainloop()
