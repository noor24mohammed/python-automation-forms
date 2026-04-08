# 🧪 Automation Testing Framework (Playwright + Excel Reporting)

## 📌 Overview

This project is an **automation testing framework** built using:

* Python 🐍
* Playwright 🎭
* OpenPyXL 📊

It automatically:

* Fills web forms
* Validates submission
* Captures screenshots
* Saves results in a **single Excel sheet**

---

## ⚙️ Features

✅ Supports multiple forms
✅ Works with different JSON formats
✅ Dynamic field handling
✅ Screenshot capture
✅ PASS/FAIL status with color
✅ Single Excel sheet (no overwrite)
✅ Auto column creation for all JSON keys

---

## 📁 Project Structure

```
Automation_testing_forms/
│
├── data/
│   ├── general.json
│   ├── enquiry.json
│   ├── saburi.json
│   ├── shankara.json
│   ├── mrceo.json
│
├── tests/
│   ├── general.py
│   ├── enquiry.py
│   ├── saburi.py
│   ├── shankara.py
│   ├── mrceo.py
│
├── utils/
│   └── excel_writer.py
│
├── screenshots/
│
├── main_runner.py
├── result.xlsx
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```
pip install playwright openpyxl
playwright install
```

---

### 2️⃣ Run the project

```
python main_runner.py
```

---

### 3️⃣ Select option

```
1. General
2. Saburi
3. Enquiry
4. Shankara
5. MRCEO
6. Run ALL
```

---

## 📊 Excel Output

All results are saved in:

```
result.xlsx
```

### Columns:

* Test Case
* Form Name
* Website
* Execution Time
* Status (PASS/FAIL)
* Screenshot
* * All JSON fields dynamically

---

## 🧠 How It Works

### 1. JSON Input

Each form has its own JSON file.

Example:

```
{
  "name": "Noor",
  "email": "test@gmail.com",
  "phone": "9876543210"
}
```

---

### 2. Form Automation

* Opens website
* Fills fields
* Submits form
* Takes screenshot

---

### 3. Excel Logging

* Loads existing Excel
* Adds new row (no overwrite)
* Creates new columns if new JSON keys appear

---

## 🎨 Status Colors

* 🟢 PASS → Green
* 🔴 FAIL → Red

---

## 📸 Screenshots

Saved inside:

```
screenshots/
```

---

## 🔥 Key Benefits

✔ No manual Excel handling
✔ Works for ANY form
✔ Dynamic field support
✔ Scalable framework

---

## 🚀 Future Improvements

* Dashboard reporting 📊
* Email reports 📧
* Parallel execution ⚡
* Database storage 🗄️

---

## 👨‍💻 Author

Mallesh N
Automation Engineer 🚀
