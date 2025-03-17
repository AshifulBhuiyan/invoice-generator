# LaTeX Invoice Generator

This is a simple Flask-based web application that generates invoices in PDF format using LaTeX. The application allows users to enter invoice details, add multiple services/items, and download a professionally formatted invoice.

## Features
- Dynamic form to add multiple services/items
- Generates a LaTeX-based PDF invoice
- Includes a customizable logo
- Uses Flask for the backend

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3
- Flask
- LaTeX (TeX Live recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AshifulBhuiyan/invoice-generator.git
   cd latex-invoice-generator
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Install LaTeX (if not already installed):
   ```bash
   sudo apt install texlive-latex-base texlive-latex-extra
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
```
latex-invoice-generator/
│── static/                  # Stores logo and other static assets
│── templates/               # HTML templates for the web interface
│   ├── index.html           # Main input form
│   ├── invoice_template.tex # LaTeX template for invoice
│── invoices/                # Stores generated invoices
│── app.py                   # Flask application
│── README.md                # Project documentation
│── .gitignore               # Git ignore file
```

## Customization
- Replace `static/logo.png` with your own logo.
- Modify `invoice_template.tex` for layout changes.