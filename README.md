# Tabulation System (Django Project)

This is a Django-based tabulation system for managing judges, candidates, criteria, and results in contests/events.

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.10** or higher
- **MySQL Server** (running on localhost:3306)
- **Git** (for cloning the repository)

## Installation

1. **Clone the repository** (if not already done):

   ```bash
   git clone <repository-url>
   cd tabulation
   ```

2. **Install Python dependencies**:
   The project uses Django and MySQL connector. Install the required packages:

   ```bash
   pip install django mysqlclient
   ```

   Additional packages that may be needed:

   ```bash
   pip install djangorestframework django-cors-headers django-cleanup django-browser-reload
   ```

3. **Set up MySQL Database**:
   - Ensure MySQL server is running on localhost:3306
   - Create a database named `tabulatormsanfermin`
   - Update database credentials in `tabulatorMsSanfermin/settings.py` if needed:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'tabulatormsanfermin',
             'USER': 'root',  # Change if different
             'PASSWORD': 'loleris1234',  # Change to your MySQL password
             'HOST': 'localhost',
             'PORT': '337',
         }
     }
     ```

## Running the Project

1. **Apply database migrations**:

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser** (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

4. **Access the application**:
   - Open your web browser and go to: `http://127.0.0.1:8000`
   - Admin interface: `http://127.0.0.1:8000/django-admin/`

## Project Structure

- `tabulatorMsSanfermin/` - Main Django project settings
- `mainapp/` - Main application with views, models, and templates
- `dbase/` - Database models and migrations
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates

## Features

- Judge management and scoring
- Candidate management
- Criteria-based evaluation
- Result calculation and reporting
- Admin panel for system management
- User authentication

## Troubleshooting

- **Database connection error**: Ensure MySQL server is running and credentials are correct
- **Migration issues**: Run `python manage.py makemigrations` if needed
- **Port conflicts**: Change the runserver port with `python manage.py runserver 8001`

## Development

To contribute or modify the project:

1. Create a virtual environment: `python -m venv venv`
2. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
3. Install dependencies as above
4. Make changes and test locally
5. Run migrations if models are modified: `python manage.py makemigrations && python manage.py migrate`
