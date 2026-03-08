# 🚦 Traffic Violation Logger (Flask)

## 📌 Project Overview

The **Traffic Violation Logger** is a lightweight web application built using Flask that helps traffic authorities digitally record, manage, and track traffic violations.

Officers can log violations by entering details such as vehicle number, violation type, location, date, and fine amount. Each violation is stored in a database and marked as **Paid** or **Unpaid**.

The system also generates a **QR code challan**, allowing the public to check fine status instantly.

---

## ✨ Features

### ✅ Add Violation Record

Traffic officers can enter:

* Vehicle Number
* Violation Type (No Helmet, Overspeeding, etc.)
* Location
* Date
* Fine Amount

All records are automatically marked **Unpaid**.

### 🔍 View Violation History

* Search by vehicle number
* View all past violations

### 🔄 Update Violation Status

* Change status from **Unpaid ➝ Paid**

### 📱 QR Code Challan

* QR generated dynamically
* Scanning shows:

  * Violation details
  * Payment status

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite + SQLAlchemy
* **Frontend:** HTML, CSS, Bootstrap
* **QR Code:** qrcode library

---
## 🎯 Learning Outcomes

* Flask routing
* CRUD operations
* Database integration using SQLAlchemy
* QR code generation
* Web application workflow design

---

## 🚀 Future Enhancements

* Login authentication for officers
* Online payment integration
* PDF challan generation
* Dashboard analytics

---

## 👩‍💻 Author

**Ramyaa Murugan**
