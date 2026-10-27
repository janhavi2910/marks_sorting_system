# Marks Sorting System

A small Flask website demonstrating Bubble Sort and Selection Sort for student marks.

## Features
- Add or edit student names and marks (0–100)
- View the original marks list
- Sort ascending or descending
- Choose Bubble Sort or Selection Sort
- See the sorted list and rank/order clearly
- Responsive HTML/CSS interface

## Run in terminal

1. Install Python 3.10 or newer.
2. Extract this ZIP and open a terminal in the `marks_sorting_system` folder.
3. (Recommended) Create a virtual environment:
   - Windows: `py -m venv .venv`
   - Activate: `.venv\Scripts\activate`
4. Install dependencies:
   `pip install -r requirements.txt`
5. Start the website:
   `python app.py`
6. Open the address printed in the terminal, usually:
   `http://127.0.0.1:5000`

Use Ctrl+C in the terminal to stop the server.

## Files
- `app.py` — Flask routes and form handling (backend)
- `sorting_algorithms.py` — Bubble Sort and Selection Sort logic
- `templates/index.html` — website structure
- `static/style.css` — styling and responsive layout
- `requirements.txt` — Python dependency
