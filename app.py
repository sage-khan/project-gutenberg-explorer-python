from flask import Flask, render_template, request, jsonify
import requests
import json
import os
import pandas as pd

app = Flask(__name__)

# Paths
BASE_URL = "https://www.gutenberg.org/files/"
DATA_FILE = "data/books.json"
CSV_FILE = "data/pg_catalog.csv"
GROQ_API_KEY = "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"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Ensure required directories exist
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Load metadata CSV
# Load metadata CSV properly
try:
    metadata_df = pd.read_csv(CSV_FILE, dtype={'Text#': str})
    metadata_df.columns = metadata_df.columns.str.strip()  # Remove spaces
    metadata_df = metadata_df.rename(columns={"Text#": "Text_ID"})  # Rename for consistency
except Exception as e:
    print(f"Error loading CSV: {e}")
    metadata_df = pd.DataFrame()

def fetch_metadata(book_id):
    """Retrieve metadata from CSV based on book ID."""
    if metadata_df.empty:
        return {"error": "Metadata CSV not loaded properly"}

    book_metadata = metadata_df[metadata_df["Text_ID"] == str(book_id)]
    if book_metadata.empty:
        return {"error": "Book ID not found in CSV"}

    return book_metadata.iloc[0].to_dict()

def fetch_book_content(book_id):
    """Retrieve book text from Project Gutenberg."""
    content_urls = [
        f"{BASE_URL}{book_id}/{book_id}-0.txt",
        f"{BASE_URL}{book_id}/{book_id}.txt"
    ]

    for url in content_urls:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
    return "Book content not available."

def analyze_text(text):
    """Send book text to Groq for analysis."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": f"Analyze this text and also give, key characters, Language, Sentiment, language it is written in, and Plot Summary: {text[:2000]}"}]
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        groq_result = response.json()

        if "choices" in groq_result:
            return {"Groq Analysis": groq_result["choices"][0]["message"]["content"]}
        else:
            return {"error": "Groq API did not return expected output"}

    except Exception as e:
        return {"error": str(e)}

def save_book_data(book_id, content, metadata):
    """Save book metadata and preview text properly."""
    try:
        with open(DATA_FILE, "r") as f:
            books = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        books = []

    # Ensure preview is always saved
    preview_text = content[:2000] if content and content.strip() else "No preview available."

    # Prevent duplicate entries
    for book in books:
        if book["Text_ID"] == book_id:
            book["preview"] = preview_text  # Update preview if missing
            break
    else:
        books.append({
            "Text_ID": book_id,
            "Title": metadata.get("Title", "Unknown"),
            "Authors": metadata.get("Authors", "Unknown"),
            "Issued": metadata.get("Issued", "Unknown"),
            "Subjects": metadata.get("Subjects", "Unknown"),
            "LoCC": metadata.get("LoCC", "Unknown"),
            "Bookshelves": metadata.get("Bookshelves", "Unknown"),
            "preview": preview_text  # Always store preview
        })

    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)

    print(f"✅ Successfully saved book {book_id} with preview!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_book', methods=['POST'])
def fetch_book():
    book_id = request.form.get('book_id')
    if not book_id or not book_id.isdigit():
        return jsonify({"error": "Valid Book ID is required"}), 400

    metadata = fetch_metadata(book_id)
    if "error" in metadata:
        return jsonify(metadata), 404

    content = fetch_book_content(book_id)
    save_book_data(book_id, content, metadata)  # Save preview along with metadata

    return jsonify({
        "Text_ID": book_id,
        "Title": metadata["Title"],
        "Authors": metadata["Authors"],
        "Issued": metadata["Issued"],
        "Subjects": metadata["Subjects"],
        "LoCC": metadata["LoCC"],
        "Bookshelves": metadata["Bookshelves"],
        "preview": content[:2000],  # Include preview in the response
        "analysis": analyze_text(content[:5000])  # Limit analysis to first 5000 chars
    })

@app.route('/get_books')
def get_books():
    """Retrieve stored book data including previews."""
    try:
        with open(DATA_FILE, "r") as f:
            books = json.load(f)

        # Ensure books have valid previews
        for book in books:
            if "preview" not in book or not book["preview"].strip():
                book["preview"] = "No preview available."

    except (json.JSONDecodeError, FileNotFoundError):
        books = []
    
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
