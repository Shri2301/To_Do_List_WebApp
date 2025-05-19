# To-Do List Web Application

A secure and user-friendly task management application built with Django. This app allows users to create, manage, and track their tasks efficiently with a focus on security and a smooth user experience.

---

**Note**: This project is hosted live on [PythonAnywhere](http://shriyash.pythonanywhere.com/user_login), where you can try it out

## Features

- Secure user authentication with email verification  
- Password recovery workflow for user convenience  
- Full CRUD operations on tasks: create, read, update, and delete  
- Mark tasks as completed by crossing them off  
- Update task details easily  
- Clean  user interface designed for smooth interaction  

---

### Prerequisites
- Python 3.x  
- Django  
- A Google account (for email verification)
- Other dependencies listed in `requirements.txt`   

## Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/your-username/todo-django-app.git
  ```

2. Install dependencies

  ```bash
  pip install -r requirements.txt
  ```

3. In td_project/settings.py, update the following values:
  ```bash
  EMAIL_HOST_USER = 'your_email@gmail.com'
  EMAIL_HOST_PASSWORD = 'your_google_app_password'
  ```
**Note:** You’ll need to generate a Google App Password to use Gmail for email verification and recovery.
Step-by-step instructions are provided in the section How to <Create a Google App Password for Email Authentication> below.

4. Apply migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

5. Run the server:
  ```bash
  python manage.py runserver
  ```

6. Access the app in your browser:
  ```bash
  Navigate to: http://127.0.0.1:8000/
  ```
  
## How to Create a Google App Password for Email Authentication

If your app needs to send emails using your Gmail account (e.g., via SMTP), and you have **2-Step Verification** enabled on your Google account, you must create an **App Password** to authenticate securely.

This guide explains how to generate a Google App Password for your application.

---

### Prerequisites
- A Google account with **2-Step Verification** enabled.
- Access to your Google account settings.

---

### Steps to Create an App Password

1. **Sign in to your Google Account**

   Go to [https://myaccount.google.com/security](https://myaccount.google.com/security) and log in.

2. **Verify that 2-Step Verification is enabled**

   - Under the **"Signing in to Google"** section, check **2-Step Verification**.
   - If it is **Off**, click it and follow the instructions to enable it.

3. **Access the App Passwords page**

   - Once 2-Step Verification is enabled, return to the **Security** page.
   - Click on **App Passwords** under the **"Signing in to Google"** section.
   - You might be asked to enter your password again.

4. **Create a new App Password**

   - In the **Select app** dropdown, choose **Other (Custom name)**.
   - Enter a descriptive name for your app (e.g., "My Hangman App").
   - Click **Generate**.

5. **Copy the generated password**

   - Google will display a 16-character app password (e.g., `abcd efgh ijkl mnop`).
   - Copy this password — **you won't see it again**.
   - Use this password instead of your regular Google account password in your app’s email settings.

6. **Use the App Password in your application**

   - When configuring SMTP or other email clients, use your full Gmail address as the username.
   - Use the generated app password as the password.

---

## Important Notes

- App passwords bypass 2-Step Verification but are limited to specific apps.
- Keep your app password secure and do **not** share it.
- If you suspect misuse, revoke app passwords at [https://myaccount.google.com/security](https://myaccount.google.com/security) → **App Passwords**.

---

### References

- [Google Account Help: Sign in using App Passwords](https://support.google.com/accounts/answer/185833)
