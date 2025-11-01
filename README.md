# Text Summarizer with Flask Backend and Chrome Extension Frontend

## Overview
This project provides a text summarization web app using a Flask backend powered by Hugging Face's Transformer models, alongside a Chrome extension frontend for easy access to the summarizer functionality directly from the browser toolbar.

Users can input or paste large texts; the backend processes and summarizes them using a BART summarization model, and the extension allows quick summarization without leaving the browser.

---

## Features
- Flask Python backend serving a text summarization API
- Uses Hugging Face Transformers (facebook/bart-large-cnn) for summarization
- Frontend web app with modern purple galaxy themed UI
- Chrome extension popup UI for easy summarization on the go
- Tokenizer-aware text chunking for handling long inputs safely
- Responsive and polished UI with CSS styling

---

## Tech Stack
- **Backend:**
  - Python 3.9+
  - Flask (Web framework)
  - Hugging Face Transformers (NLP models)
  - PyTorch (Deep learning backend)
  - Conda for environment management

- **Frontend:**
  - HTML / Jinja2 (Flask templates)
  - CSS (purple galaxy & cotton candy themes)
  - JavaScript (for Chrome extension integration)

- **Chrome Extension:**
  - Manifest V3
  - Popup HTML/CSS/JS calling Flask API
  - Runs in Google Chrome browser

---

## Installation & Setup

### Backend Setup
1. Clone the repo.
2. Create and activate Conda environment:
conda create -n myenv python=3.9 -y
conda activate myenv
3. Install dependencies:
pip install -r requirements.txt
4. Run the Flask app:
python app.py

### Frontend
- Web templates are available in `templates/` folder.
- Static CSS files in `static/`.

### Chrome Extension
1. Navigate to `chrome-extension/` folder (provided).
2. Load unpacked extension in Chrome `chrome://extensions` by selecting this folder.
3. Ensure Flask backend is running and accessible at the URL specified in extension manifest.

---

## Usage

- **Web App:** Access at `http://127.0.0.1:5000` in your browser.
- **Chrome Extension:** Click the extension icon and paste text in popup, then click "Summarize" to get the summary.

---

## Notes

- Model input length limited to ~1024 tokens; large inputs are chunked accordingly.
- Flask app uses a simple development server; not suitable for production as is.
- You may deploy Flask backend on cloud services and update extension manifest accordingly.

---


## Acknowledgments

- Hugging Face Transformers for powerful NLP models.
- Chrome Extensions team for great developer APIs.

---

Feel free to contribute or raise issues!

