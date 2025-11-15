# TLC
### Collaboration Note:
All changes, updates, and improvements to this project are made together during personal meetings or online calls via Microsoft Teams.
This means that every part of the development — including code, design, documentation, and updates — is the result of equal collaboration (50/50 work) between both project creators.
It does not matter who commits or uploads the changes; all work is done jointly.

## TLC — The Loin Coin

TLC (The Loin Coin) is a web-based crypto simulation platform built with Python (Django).
It allows users to explore how a cryptocurrency website works — including balance management, buying and selling a fictional coin, and viewing live graph updates that react to simulated market activity.

A visual concept sketch of the website design is included in the repository.
The design will evolve during development as the project improves.

## Project Description

TLC is an educational and experimental crypto project created to simulate a functioning cryptocurrency environment in a safe and controlled way.
Users can:

View information about the project and its creators

Deposit and withdraw funds (simulated)

Buy and sell the TLC coin — all transactions are artificial

See a dynamic price graph that changes depending on buy/sell activity

This simulation provides an engaging way to learn about the logic behind trading systems and web development.

| Technology          | Purpose                                              |
| ------------------- | ---------------------------------------------------- |
| **Python (Django)** | Backend logic and routing                            |
| **HTML**            | Page structure                                       |
| **CSS**             | Styling and visual layout                            |
| **JavaScript**      | Interactivity and dynamic updates                    |
| **SQLite**          | Local database for storing user and transaction data |
| **VS Code**         | Development environment                              |

## Features

Simulated Wallet System — Users can top up and see balance changes.

Buy & Sell TLC Coin — Fully artificial, for educational demonstration.

Dynamic Graph — The coin’s price graph rises or falls based on user transactions.

Project Info Section — Explains how TLC was built and the technologies behind it.

Responsive Design — Optimized for different screen sizes.

## Project Structure
### 📂 Project Structure

```text
TLC-CRYPTOCURRENCY/
│
├── Design_elements/                # Design assets and visual elements
│   ├── TLC_animation.mp4           # Animation for presentation/demo
│   └── TLC_design.png              # UI design reference
│
├── env/                            # Virtual environment (excluded from version control)
│
├── TLCapp/                         # Main Django application
│   ├── migrations/                 # Database migration files
│   ├── static/                     # Static files (CSS, JS)
│   │   └── css/                    # Styling for frontend pages
│   │       ├── home.css
│   │       ├── main.css
│   │       └── singup_in.css
│   ├── templates/                  # HTML templates for the app
│   │   ├── home.html
│   │   ├── main.html
│   │   ├── singin.html
│   │   └── singup.html
│   ├── __init__.py                 # Marks the folder as a Python package
│   ├── admin.py                    # Django admin panel configuration
│   ├── apps.py                     # Application configuration
│   ├── forms.py                    # User forms (login, signup)
│   ├── models.py                   # Database models (User, Wallet, Transaction)
│   ├── tests.py                    # Unit and integration tests
│   ├── urls.py                     # URL routing for the app
│   └── views.py                    # View logic and request handling
│
├── TLCproject/                     # Django project configuration
│   ├── __init__.py
│   ├── asgi.py                     # ASGI entry point (async support)
│   ├── settings.py                 # Global Django settings
│   ├── urls.py                     # Root project URLs
│   └── wsgi.py                     # WSGI entry point (deployment)
│
├── db.sqlite3                      # Local SQLite database
├── manage.py                       # Django management script (runserver, migrate, etc.)
├── LICENSE                         # Project license information
└── README.md                       # Project documentation

```

## Sketch
<img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/e7d1631d-9166-4b30-9414-1b55e7280d48" />

## Future Improvements

User authentication system

Enhanced visual design and animations

## About the Project

TLC — The Loin Coin — was created as a creative and educational project to understand cryptocurrency logic, user interface design, and full-stack web development.
The website is a fictional simulation meant for learning and demonstration purposes only.

TLC — The Loin Coin — was created as a creative and educational project to understand cryptocurrency logic, user interface design, and full-stack web development.
The website is a fictional simulation meant for learning and demonstration purposes only.
