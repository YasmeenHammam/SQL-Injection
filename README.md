# SQL Injection Detector

A Python package to detect SQL injection attempts using a Flask-based web application.

## Installation

Follow these steps to install and use the SQL Injection detection package in your Flask app:

### 1. Clone the Repository:

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/YasmeenHammam/SQL-Injection
```

### 2. Navigate to Your Existing Flask App Directory:

Open a terminal and navigate to the directory where your Flask app is located.

```bash
cd /path/to/your/flask-app
```

### 3. Set Up a Virtual Environment:

If you don't already have a virtual environment for your Flask app, you can create and activate one:

- Create a virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate the virtual environment:
  For Git Bash or WSL (Unix-like shell on Windows):
  ```bash
  source venv/Scripts/activate
  ```

  For Windows Command Prompt:
  ```bash
  venv\Scripts\activate
  ```

  For Windows PowerShell:
  ```bash
  .\venv\Scripts\Activate
  ```

  For Linux/MacOS:
  ```bash
  source venv/bin/activate
  ```

Note: After activation, you should see (venv) at the start of your command line, indicating that the virtual environment is active.

### 4. Install the SQL Injection Detection Package:

install the package using pip by providing the path to the cloned SQL-Injection directory:

```bash
pip install /path/to/SQL-Injection
```

Replace /path/to/SQL-Injection with the actual path to where you cloned the SQL-Injection repository.

### 5. Import and Use the Middleware Function in Your Flask App:

In your Flask application script, import the waf function from the package:

```bash
from sql_injection_detector import waf
```

### 6. Register the Middleware with Your Flask App:

Add the waf middleware to your Flask app to protect against SQL injection:
```bash
app.before_request(waf)
```

This line should be added after you create your Flask app instance (app = Flask(**name**)) to ensure that the waf function runs before each request.
