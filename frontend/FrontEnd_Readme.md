# Stationery Store Frontend

## Project Structure

The frontend code is organized within the `frontend` directory, which contains the CSS, JavaScript, and HTML template files.

```bash
frontend/
├── css/
│ └── styles.css
├── js/
│ └── scripts.js
├── templates/
│ ├── inventory/
│ │ ├── base.html
│ │ ├── stationery_list.html
│ │ ├── stationery_detail.html
│ │ ├── stationery_form.html
│ │ ├── stationery_confirm_delete.html
```

### CSS

- **styles.css**: Contains the custom styles for the application.

### JavaScript

- **scripts.js**: Contains custom JavaScript for the application.

### Templates

The HTML templates for the application are stored in the `frontend/templates/inventory` directory.

- **base.html**: The base template that includes common HTML structure and static file references.
- **stationery_list.html**: Template for displaying the list of stationery items.
- **stationery_detail.html**: Template for displaying the details of a single stationery item.
- **stationery_form.html**: Template for creating and editing stationery items.
- **stationery_confirm_delete.html**: Template for confirming the deletion of a stationery item.

## Libraries Used

- **Bootstrap**: For responsive design and consistent styling.
- **jQuery**: For simplified JavaScript operations (included via CDN in the templates).

## Instructions for Running

The frontend code relies on Django to serve the HTML templates and static files (CSS and JavaScript). Here are the steps to run the frontend as part of the Django project:

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   venv\Scripts\activate`
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

- The code is organized into templates and static files.
- Proper comments and documentation are included.
- The project follows best practices for HTML, CSS, and JavaScript.

## Testing

- Basic testing has been done to ensure there are no major bugs or issues.
