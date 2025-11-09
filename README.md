# 🚗 Car Rental Management System (PHP/MySQL)

## 💡 Overview

This project implements a robust, full-stack web-based **Car Rental Management System**. It is designed to facilitate efficient fleet management, customer booking, and administrative oversight. The system features separate, secure interfaces for both customers and administrators.

It is built upon the classic and reliable **PHP/MySQL** stack, making it easy to deploy on any standard LAMP/WAMP environment.

> **Note on Project History:**
> This repository represents a revival and renewed commitment to this system, which was **originally developed in [Year of original development, e.g., 2022]**. We are focused on ongoing maintenance and potential feature enhancements.

## ✨ Key Features

### Management & Control (Admin Portal)

* **Fleet Management (CRUD):** Complete control to add, view, update, and delete vehicle records from the inventory (`addcar.php`, `deletecar.php`).
* **Booking Lifecycle:** Review, approve, or cancel customer bookings (`adminbook.php`, `approve.php`, `adminreturn.php`).
* **User Management:** Oversee and manage all registered customer accounts (`adminusers.php`, `deleteuser.php`).
* **Central Dashboard:** A secure, single-page view for key system metrics (`admindash.php`).

### Customer Experience (Client Portal)

* **Secure Authentication:** User registration and login functionality (`register.php`, `index.php`).
* **Vehicle Catalog:** Browse available cars and view detailed specifications (`cardetails.php`).
* **Booking System:** Request a rental by specifying dates and completing the booking process (`booking.php`).
* **Status Tracking:** View the current status of submitted rental requests (pending, approved, returned) (`bookinstatus.php`).
* **Payment Flow:** Integration for handling rental payment processing (`payment.php`, `psucess.php`).

## 💻 Technology Stack

| Category | Technology | Files Included |
| :--- | :--- | :--- |
| **Backend** | **PHP** | `*.php` files (approx. 57% of codebase) |
| **Database** | **MySQL / MariaDB** | `database/` folder, `connection.php` |
| **Frontend** | **HTML5 & CSS3** | `*.html`, `css/` folder |
| **Scripting** | **JavaScript** | `main.js` |
| **Environment**| **XAMPP / WAMP / LAMP** | Required runtime environment |

## 🚀 Installation Guide

This guide details how to set up the Car Rental Management System on a local development environment (e.g., XAMPP, WAMP).

### Prerequisites

* A running **Apache** web server.
* **PHP** installed.
* **MySQL** database server running.

### 1. Repository Setup

1.  **Clone the Project:** Place the project files into your web server's document root (e.g., `htdocs` for XAMPP).
    ```bash
    git clone [https://github.com/Inesh-Makhija/CarRental.git](https://github.com/Inesh-Makhija/CarRental.git)
    ```

### 2. Database Configuration

1.  **Create Database:** Access your MySQL administrative tool (like phpMyAdmin) and create a new database.
2.  **Import Schema:** Import the SQL script found in the `database/` folder into your new database. This creates all necessary tables (`users`, `cars`, `bookings`, etc.).
3.  **Update Connection:** Edit the `connection.php` file to match your local database credentials (username, password, and database name).

### 3. Access the Application

Once the database and connection files are configured, you can access the application through your local URL:

| Portal | Entry URL |
| :--- | :--- |
| **Client Interface** | `http://localhost/CarRental/index.php` |
| **Admin Panel Login** | `http://localhost/CarRental/adminlogin.php` |

## 🤝 Support & Contributing

While this project is not set up for financial contributions, we welcome community involvement.

* **Issues:** If you find any bugs or have feature suggestions, please open an issue in the repository.
* **Contributions:** Feel free to fork the repository, make improvements, and submit a Pull Request.

## 📄 License

This project is open-source and released under the **MIT License**.

See the [LICENSE](LICENSE) file for more details.