# OpenLeaf 🌿

OpenLeaf is a full-stack **Flask web application** that allows users to create, manage, and interact with blog posts. It includes secure authentication, password reset functionality, and user profiles. This project demonstrates modern web development practices using Python and Flask.

---

## Features

- **User Authentication**
  - Sign up and login with secure password hashing
  - Session management using Flask-Login
- **Password Reset**
  - Token-based password reset via email
  - Expiring tokens for enhanced security
- **Posts**
  - Create, read, update, and delete blog posts
  - Pagination for browsing posts
- **User Profiles**
  - Upload profile pictures
  - View own posts
- **Security**
  - CSRF protection via Flask-WTF
  - Hashed passwords
  - Token-based operations for sensitive actions

---

## Tech Stack

- **Backend:** Python, Flask, Flask-Login, Flask-WTF, SQLAlchemy  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, Bootstrap 
- **Email:** Flask-Mail (for password reset)  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/openleaf.git
cd openleaf
Create and activate a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Set environment variables in .env (optional if using Gmail for emails):

SECRET_KEY=your_secret_key
MAIL_USERNAME=yourgmail@gmail.com
MAIL_PASSWORD=your_app_password
Run the application:

python run.py
Open in browser:

http://127.0.0.1:5000/
Usage
Register a new account or log in with existing credentials

Create, edit, or delete your blog posts

Reset your password via email link if needed

View posts from all users

Contributing
Contributions are welcome! If you want to add features or improve OpenLeaf:

Fork the repository

Create a new branch (git checkout -b feature-name)

Make your changes

Commit (git commit -m 'Add new feature')

Push (git push origin feature-name)

Open a Pull Request

License
This project is open-source and available under the MIT License.

Contact
Created by [Your Name]
Email: your-email@example.com
GitHub: github.com/YOUR-USERNAME


1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/openleaf.git
cd openleaf
