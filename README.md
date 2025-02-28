# project-gutenberg-explorer-python

This is the codebase of take-home assignment given by SarjAI. We will be making this completely in Python, although we do have some versions available in JS/TS.

## Directory Structure

This is the directory structure
---

### 📂 Project Directory Structure:
```
Project_Gutenberg_Explorer/
│── app/                     # Main application folder
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates for the frontend
│   ├── __init__.py          # Makes the folder a Python package
│   ├── routes.py            # Flask routes for handling requests
│   ├── models.py            # Data models and database interactions (if needed)
│   ├── gutenberg_api.py      # Functions for fetching and processing books
│   ├── text_analysis.py      # Text analysis functions using LLMs
│   ├── utils.py              # Utility functions
│
│── scripts/                 # Scripts for one-time setups (if required)
│   ├── download_catalog.py  # Script to fetch Gutenberg catalog locally
│
│── config.py                # Configuration settings
│── run.py                   # Flask app entry point
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
```

---

### 📜 **Description**
- **`app/`** → The main application folder
  - **`static/`** → Contains CSS, JS, and images for the web UI.
  - **`templates/`** → Holds HTML templates for displaying books and search results.
  - **`routes.py`** → Defines Flask API routes, handles user requests.
  - **`models.py`** → (Optional) Defines database models if you store book metadata.
  - **`gutenberg_api.py`** → Handles fetching book metadata and downloading e-books.
  - **`text_analysis.py`** → Implements text summarization, topic modeling, etc.
  - **`utils.py`** → Utility functions (e.g., formatting text, caching results).

- **`scripts/`** → Holds scripts for one-time tasks (e.g., downloading metadata).
  - **`download_catalog.py`** → Fetches and stores Project Gutenberg’s book catalog locally.

- **`config.py`** → Stores app configurations (API keys, file paths).

- **`run.py`** → The main Flask application entry point.

- **`requirements.txt`** → List of dependencies (Flask, requests, transformers, etc.).

- **`README.md`** → Project documentation.

---

