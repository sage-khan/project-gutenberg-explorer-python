# Project Gutenberg Explorer

## **Overview**

Project Gutenberg is a platform to download and access free e-books. We're looking to build a web application that allows users to explore and analyze books from Project Gutenberg.

[Project Gutenberg - Example Book](https://www.gutenberg.org/ebooks/1787)

Our project aims to download books, display them, and analyze the text using LLMs.

**Deadline:** 1 week from starting

## **API Access**

E-book content and metadata can be programmatically fetched via Project Gutenberg:

```python
import requests

book_id = "1787"
content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
metadata_url = f"https://www.gutenberg.org/ebooks/{book_id}"

# Get book content
content_response = requests.get(content_url)
content = content_response.text

# Get metadata
metadata_response = requests.get(metadata_url)
```

## **Requirements**

### ⚙️ Core Functionality

1. Input field for users to enter a Project Gutenberg book ID.
2. Fetch and display the book's text and metadata.
3. Save the book text and metadata for future access.
4. Provide a list view of all books the user has previously accessed.

### 🧠 Text Analysis

Given the text, users should be able to perform text analysis. You are free to choose what analysis you find most interesting, but some possible features include:

- Identifying key characters
- Language Detection
- Sentiment Analysis
- Plot Summary
- Additional custom analysis

### 💅 Styling

Style the application as you see fit. We personally recommend using Tailwind and Shadcn for a clean and modern UI.

### 👨‍💻 Deliverables

- Deploy the application to the internet.
- Integrate an LLM for text analysis (you have flexibility in choosing the specific model).
- Store source code in GitHub.
- Create a Loom video walkthrough explaining the application and technical choices.

💡 **Free LLM Providers:**

Two excellent and free LLM providers are:

- [Groq](https://groq.com/)
- [SambaNova](https://cloud.sambanova.ai/)

You can create accounts without credit cards, and they offer fairly generous free tiers.

