# Django CRUD App Stationery Inventory Management System

## Project Overview

This project is a simple CRUD (Create, Read, Update, Delete) application for managing stationery items in a store. It uses Django for the backend and HTML, CSS, and JavaScript for the frontend. The application allows users to view a list of stationery items, add new items, update existing items, and delete items. The purpose of this project is to provide a basic example of how to build a CRUD application using Django and to demonstrate best practices in web development.

## Project Structure

The project is structured into backend and frontend components to separate concerns and improve maintainability.

```bash
stationery_store/
├── backend/
│ ├── inventory/
│ │ ├── migrations/
│ │ │ └── init.py
│ │ ├── init.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── forms.py
│ │ ├── models.py
│ │ ├── tests.py
│ │ ├── urls.py
│ │ ├── views.py
│ ├── stationery_store/
│ │ ├── init.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ ├── wsgi.py
│ ├── db.sqlite3
│ ├── manage.py
├── frontend/
│ ├── css/
│ │ └── styles.css
│ ├── js/
│ │ └── scripts.js
│ ├── templates/
│ │ ├── inventory/
│ │ │ ├── base.html
│ │ │ ├── stationery_list.html
│ │ │ ├── stationery_detail.html
│ │ │ ├── stationery_form.html
│ │ │ ├── stationery_confirm_delete.html
└── README.md
```

## Technologies Used

### Backend

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Frontend

- **HTML**: The standard markup language for creating web pages.
- **CSS**: A stylesheet language used for describing the presentation of a document written in HTML.
- **JavaScript**: A programming language commonly used to create dynamic and interactive web experiences.

### Libraries

- **Bootstrap**: A free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.

## Project Features

- **List Stationery Items**: View all stationery items in the store.
- **Add New Item**: Add a new stationery item to the store.
- **Edit Item**: Update details of an existing stationery item.
- **Delete Item**: Remove a stationery item from the store.

## Installation Instructions

### Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- **Django**

### Steps to Run the Project

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd stationery_store
   ```

2. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

3. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install the necessary Python packages**:

   ```bash
   pip install django
   ```

5. **Run migrations to set up the database**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Django development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Project Structure and Files

### Directory Structure

- **backend/**: Contains the Django project and app files.
  - **inventory/**: Django app for managing stationery items.
    - **migrations/**: Database migrations.
    - **templates/**: HTML templates for the app (located in `frontend/templates/inventory`).
    - `__init__.py`: Initializes the app.
    - `admin.py`: Admin site configurations.
    - `apps.py`: App configuration.
    - `forms.py`: Django forms for the app.
    - `models.py`: Database models.
    - `tests.py`: Tests for the app.
    - `urls.py`: URL configurations for the app.
    - `views.py`: Views for handling web requests.
- **stationery_store/**: Main Django project.
  - `__init__.py`: Initializes the project.
  - `settings.py`: Project settings.
  - `urls.py`: URL configurations for the project.
  - `wsgi.py`: WSGI configuration for deployment.
- **frontend/**: Contains static files and templates.
  - **css/**: Custom CSS files.
    - `styles.css`: Stylesheet for the project.
  - **js/**: Custom JavaScript files.
    - `scripts.js`: JavaScript for the project.
  - **templates/**: HTML templates.
    - **inventory/**: Templates for the inventory app.
      - `base.html`: Base template.
      - `stationery_list.html`: Template for listing stationery items.
      - `stationery_detail.html`: Template for viewing details of a stationery item.
      - `stationery_form.html`: Template for adding/editing a stationery item.
      - `stationery_confirm_delete.html`: Template for confirming deletion of a stationery item.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Command-line utility for administrative tasks.

### Notes

- **Static Files**: Ensure that the paths to static files (CSS and JS) in your `base.html` template are correct. Use Django's static file handling system.
- **Admin Interface**: If you created a superuser, you can access the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

### Contributing

If you wish to contribute to this project, please fork the repository and create a pull request with your changes.
