# Stationery Store Backend

## Project Structure

The backend code is organized within the `backend` directory, which contains the Django application files and configurations.

```bash
backend/
├── inventory/
│ ├── migrations/
│ │ └── init.py
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── stationery_store/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── db.sqlite3
├── manage.py
```

### Django Apps

- **inventory**: Contains the main application logic for the stationery store, including models, views, forms, and URLs.
- **stationery_store**: Contains the project settings and configurations.

### Key Files

#### `manage.py`

The command-line utility for interacting with the Django project.

#### `inventory/`

- **admin.py**: Registers models with the Django admin site.
- **apps.py**: Configuration for the `inventory` app.
- **forms.py**: Contains form classes for the `inventory` app.
- **models.py**: Defines the database models for the `inventory` app.
- **tests.py**: Contains test cases for the `inventory` app.
- **urls.py**: Defines the URL patterns for the `inventory` app.
- **views.py**: Contains the view functions for the `inventory` app.

#### `stationery_store/`

- **settings.py**: Contains the project settings and configurations.
- **urls.py**: Defines the root URL patterns for the project.

## Libraries Used

- **Django**: The web framework used to build the application.

## Instructions for Running

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the necessary Python packages**:

   ```bash
   pip install django
   ```

4. **Run migrations to set up the database**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Django development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Code Quality

- The code follows Django best practices.
- Proper comments and documentation are included.
- The project structure is organized for maintainability and scalability.

## Testing

- Basic testing has been done to ensure there are no major bugs or issues.
