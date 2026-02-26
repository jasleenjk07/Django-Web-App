# Django Notes App

A full-stack web application for creating, viewing, editing, and deleting notes. Built with Django 6.0 as a practical introduction to web development with Python.

## Features

- **Create** — Add new notes with a title and description
- **Read** — View all notes on a responsive home page
- **Update** — Edit existing notes
- **Delete** — Remove notes you no longer need
- **Feedback** — Success and error messages for user actions
- **Responsive UI** — Clean design with Bootstrap 5 and Font Awesome icons

## Tech Stack

- **Backend:** Django 6.0.1
- **Database:** SQLite3
- **Frontend:** Bootstrap 5, Font Awesome
- **Python:** 3.13+

## Project Structure

```
Django/
├── app/                    # Main application
│   ├── models.py           # Note model
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   ├── templates/
│   │   ├── base.html       # Base layout
│   │   ├── index.html      # Home page
│   │   ├── edit_page.html  # Edit form
│   │   ├── about.html
│   │   └── components/     # Navbar, footer, messages
│   └── static/             # CSS, JS
├── project/                # Django project config
│   ├── settings.py
│   └── urls.py
├── manage.py
└── db.sqlite3
```

## Prerequisites

- Python 3.10 or higher
- pip

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd LPU_PEP
   ```

2. **Navigate to the Django project**

   ```bash
   cd Django
   ```

3. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install Django**

   ```bash
   pip install django
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

## Running the Application

```bash
cd Django
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- **Home (/)** — Add new notes and view all notes
- **Add Note** — Fill in the title and description, then click "Add Note"
- **Edit** — Click "Edit" on any note card to modify it
- **Delete** — Click "Delete" on any note card to remove it
- **About (/about)** — Visit the about page

## License

This project is open source and available for educational purposes.
