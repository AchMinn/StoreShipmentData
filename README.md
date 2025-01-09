
# Shipment Data Manager

This is a Flask web application for managing shipment data. Users can fill out a form to record shipment details, which are saved in a CSV file.

### You can remove the csv file after cloning it's useless

## Features

- Input shipment data through a user-friendly web form.
- Validate input data before saving.
- Store data in a CSV file for easy access.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository** :
   If you have a Git repository, clone it. Otherwise, create a directory for your project.

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   It's a good practice to create a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install Flask and other required libraries using the provided `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the Project Structure**:
   Ensure the following files and directories are created in your project directory:

   ```
   /path/to/your/project/
   ├── app.py                # Your Flask application
   ├── templates/            # Directory for HTML templates
   │   └── index.html        # Main HTML file
   ├── static/               # Directory for static files (CSS)
   │   └── index.css         # CSS file for styling
   └── requirements.txt      # Python dependencies
   ```


5. **Create the CSV File**:
   The application will automatically create a CSV file named `dati_carico.csv` in the project directory upon the first run.

6. **Run the Application**:
   Start the Flask development server by running:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:3214`.

7. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:3214` to access the Shipment Data Manager.

## Usage

1. Fill out the form with the shipment details.
2. Click the "Add Shipment" button to submit the form.
3. The data will be validated and appended to the CSV file.

## Notes

- Ensure that the application has write permissions to the directory where it is run to create the CSV file.
- For production use, consider deploying the application with a WSGI server like Gunicorn.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
