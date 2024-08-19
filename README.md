# Topics-in-Network-Security

How to use the tool ?
# Step 1: Clone the Git Repository
git clone git@github.com:YasmeenHammam/SQL-Injection.git

# Step 2: Navigate into the project directory
cd SQL-Injection

# Step 3: Set Up Python Virtual Environment
python -m venv venv

# Step 4: Activate the Virtual Environment
source venv/Scripts/activate

# Step 5: Install Dependencies from requirements.txt
pip install -r requirements.txt

# Step 6: Run the SQL Injection Detection Tool using Waitress
waitress-serve --port=8000 app:app