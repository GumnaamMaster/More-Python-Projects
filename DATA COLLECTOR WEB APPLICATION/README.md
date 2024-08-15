# Flask Height Collector Application

This project is a Flask-based web application designed for collecting height data, managing file uploads, and sending email notifications. The application allows users to submit their height data, upload files, and download the processed files. It also includes email functionality to notify users with their height information and statistics.

## Features

- **Submit Height Data**: Users can submit their height along with their email address.
- **File Upload**: Users can upload files which are saved and modified on the server.
- **File Download**: Users can download the uploaded and processed files.
- **Email Notifications**: Sends email notifications with height data and statistics to users.
- **Data Storage**: Uses PostgreSQL for storing user data.

## Project Structure

- `script.py`: The main Flask application file.
- `send_mail.py`: Contains the email sending functionality.
- `templates/`: Directory containing HTML templates (`index.html`, `download.html`).

## Setup and Installation

### Prerequisites

- Python 3.x
- PostgreSQL database
- Required Python packages

### Installation Steps

1. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. Install Dependencies

pip install -r requirements.txt

Make sure to include Flask, Flask-SQLAlchemy, and other necessary packages in your requirements.txt.

3. Set Up the Database

Ensure PostgreSQL is installed and create a database. Update the SQLALCHEMY_DATABASE_URI in script.py with your PostgreSQL credentials:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://username:password@localhost/dbname'

4. Run the Flask Application

python script.py

The application will be available at http://127.0.0.1:5000/.

5. Email Configuration

Update the email credentials in send_mail.py with your actual email and password:

from_email = "your-email@gmail.com"
from_password = "your-email-password"

Ensure that "Less secure app access" is enabled for Gmail or use an app-specific password.

Usage
Submit Height Data

Navigate to the home page.
Enter your email and height.
Submit the form.
Upload and Modify Files

On submission, you will be redirected to a page where you can upload a file.
The file will be saved and modified on the server.
Download Processed Files

After uploading, you can download the processed file by clicking the provided link.
Email Notifications

After submitting your height data, you will receive an email with your height and some statistics.
Troubleshooting
Method Not Allowed Error: Ensure that POST methods are correctly specified in route decorators. Check the form method in your HTML templates.
Database Connection Issues: Verify PostgreSQL is running and the database URI is correctly set.
Contributing
Feel free to fork the repository and submit pull requests. For any issues or feature requests, open an issue in the repository.
