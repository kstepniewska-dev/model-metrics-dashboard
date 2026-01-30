# ML Model Metrics Dashboard
Flask-based web app for uploading CSV files (confusion matrix), calculating and visualizing ML model metrics (accuracy, precision, recall)

## Dependencies
- **Flask (with jinja2)** for views creation and backend
- **Flask-SQLAlchemy** for database support
- **pandas (with numpy)** for data analisys
- **matplotlib** for plot creation

## How to run the app
### Please, mind that below commands might behave differently depending on OS, python version, etc.
1. Create virtual environment
    - create venv **Bash**:
        `python -m venv .venv` or `python3 -m venv .venv`
    - activate venv **Bash**:
        `source .venv/Scripts/activate` or `source .venv/bin/activate`

2. Install dependencies from *requirements.txt*
    - install libs **Bash**:
    	`pip install -r requirements.txt`

3. Run the app
    - launch run.py **Bash**:
        `python run.py`or `python3 run.py`

4. Open web browser
    - browse: 
        `127.0.0.1:5000`
