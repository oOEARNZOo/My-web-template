# แสดงตัวเลือกเพศ
print("กรุณาเลือกเพศของคุณ:")
print("1 = ชาย")
print("2 = หญิง")

# รับค่าการเลือกเพศ
gender_input = input("กรอกหมายเลขที่ตรงกับเพศของคุณ: ").strip()

# ตรวจสอบเพศ
if gender_input == "1":
    gender = "ชาย"
elif gender_input == "2":
    gender = "หญิง"
else:
    gender = "ไม่ระบุ"

# รับข้อมูลส่วนสูงและน้ำหนัก
weight = float(input("กรุณาใส่น้ำหนัก (กิโลกรัม): "))
height_cm = float(input("กรุณาใส่ส่วนสูง (เซนติเมตร): "))

# แปลงส่วนสูงเป็นเมตร
height_m = height_cm / 100

# คำนวณ BMI
bmi = weight / (height_m ** 2)

# แสดงผลลัพธ์
print(f"\nเพศ: {gender}")
print(f"ค่า BMI ของคุณคือ: {bmi:.2f}")

# ตีความตามเพศ
if gender == "ชาย":
    if bmi < 18.5:
        status = "ผอม"
    elif bmi < 24.9:
        status = "ปกติ"
    elif bmi < 29.9:
        status = "น้ำหนักเกิน"
    else:
        status = "อ้วน"
elif gender == "หญิง":
    if bmi < 18.0:
        status = "ผอม"
    elif bmi < 23.9:
        status = "ปกติ"
    elif bmi < 28.9:
        status = "น้ำหนักเกิน"
    else:
        status = "อ้วน"
else:
    status = "ไม่สามารถประเมินผลได้"

# แสดงผลการประเมิน
print(f"อยู่ในเกณฑ์: {status}")
