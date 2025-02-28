# project-gutenberg-explorer-python

### **Overview**

Project Gutenberg ****is a platform to download and access free e-books. We're looking to build a web application that allows users to explore and analyze books from Project Gutenberg. 

https://www.gutenberg.org/ebooks/1787

Our project is to download books, display them and analyze the text using LLMs.

**Deadline:**  1 week from starting

---

### API Access

E-book content and metadata can be programmatically fetched via Project Gutenberg

```python
content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
metadata_url = f"https://www.gutenberg.org/ebooks/{book_id}"

# Get book content
content_response = requests.get(content_url)
content = content_response.text

# Get metadata
metadata_response = requests.get(metadata_url)
```

---

### **Requirements**

**⚙️ Core Functionality** 

1. Input field for users to enter a Project Gutenberg book ID.
2. Fetch and display the book's text and metadata.
3. Save the book text and metadata for future access.
4. Provide a list view of all books the user has previously accessed.

🧠 **Text Analysis**

Given the text the user should be able to perform text analysis. You are free to choose what analysis you find most interesting but some could be:

- Identify key characters
- Language Detection
- Sentiment Analysis
- Plot Summary
- Something else?

💅 **Styling**

Style it as you see fit. We personally really like tailwind and Shadcn.

👨‍💻  **Deliverables**

- Deploy the application to the internet
- Integrate an LLM for text analysis (you have flexibility in choosing the specific model).
- Store source code in Github
- Create a loom that walks a user through the application and explains any technical choices

<aside>
💡

Two very cool and free LLM providers are:

- https://groq.com/
- https://cloud.sambanova.ai/

You can create accounts w/o credit cards and they have fairly generous free tiers

</aside>

_Note: This is the codebase of take-home assignment given by SarjAI. We will be making this completely in Python/Flask, although we do have some versions available in JS/TS._

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

