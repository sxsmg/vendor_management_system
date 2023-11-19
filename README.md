# Django Vendor Management System

This Django-based Vendor Management System is designed to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed
- pip (Python package manager)
- Virtualenv (optional but recommended for creating isolated Python environments)

## Installation

Follow these steps to install the application:

1. **Clone the Repository**
   ```bash
   git clone https://your-repository-url.git
   cd vendor_management_system

2. **Create and Activate a Virtual Environment (Optional)**
    
    For Unix or MacOS:
    ```bash 
    virtualenv venv
    source venv/bin/activate
    ```
    For Windows:
    ```cmd
    virtualenv venv
    .\venv\Scripts\activate
    ```
3. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```
4. **Database Setup**
    By default, the project uses SQLite. If you wish to use another database, update the DATABASES setting in settings.py.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create an Admin User**
    Create a superuser if you want using:
    
    ```bash
    python manage.py createsuperuser
    ```

6. **Running the Application**
    Start the Development Server

    ```bash
    python manage.py runserver
    ```
    The application will be available at http://127.0.0.1:8000/.

7. **Accessing the Admin Panel**

    Navigate to http://127.0.0.1:8000/admin.
    Use the superuser credentials created earlier to log in.
    API Usage
    The system provides a RESTful API for managing vendors and purchase orders. Here are some of the available endpoints:

8. **API Endpoints**

    import the api collection into your postman
    
    ```bash
    POST /api/vendors/: Create a new vendor.
    GET /api/vendors/: List all vendors.
    POST /api/purchase_orders/: Create a new purchase order.
    GET /api/purchase_orders/: List all purchase orders.
    GET /api/vendors/{vendor_id}/performance: Retrieve a vendors performance metrics.
    ```

    

