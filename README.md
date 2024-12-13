# Bible PDF Reader

A web-based PDF reader application specifically designed for reading and searching through Bible PDFs. Built with Python Flask and PyPDF2.

## Features

- Clean, modern web interface
- Quick PDF selection from dropdown menu
- Full text search functionality
- Context-aware search results
- Real-time content display
- Pre-loaded Bible PDFs

## Tech Stack

- Python 3.x
- Flask
- PyPDF2
- HTML/CSS
- JavaScript

## Project Structure


pdf_reader_python_v1/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── index.html
└── bible/             # PDF storage directory
    ├── bible1.pdf
    └── bible2.pdf


## Installation

1. Clone the repository

git clone https://github.com/joshhy12/pdf_reader_python_v1.git


2. Install required packages

pip install flask PyPDF2


3. Place your PDF files in the bible folder

4. Run the application

python app.py


5. Access the application at http://127.0.0.1:5000

## Usage

1. Select a PDF from the dropdown menu
2. View the PDF content in the browser
3. Use the search bar to find specific terms
4. View search results with context

## Development

The application uses:

- Flask for the backend server
- PyPDF2 for PDF processing
- Vanilla JavaScript for frontend interactions
- Custom CSS for styling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use and modify for your own projects!
