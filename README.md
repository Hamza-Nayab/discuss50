# Discuss 50 Web Application

## Video Demo
[Watch Video Demo](https://submit.cs50.io/users/Hamza-Nayab/cs50/problems/2023/x/project)

## Description
Discuss 50 is a Flask web application modeled after Finance 50. It allows users to register, log in, provide responses for each week of the CS50 bootcamp, and view previous responses and the index. The application is built using Flask, Bootstrap, and SQLite3 database. SQL injection attacks are prevented to ensure security.

## Features
- **User Registration**: Users can register by providing their information, and their passwords are securely hashed and stored in the database.
- **User Authentication**: Users can log in securely using their credentials.
- **Week-wise Responses**: Users can provide responses for each week of the CS50 bootcamp.
- **Index Display**: The index displays the difficulty of each week in percentage using a progress bar.
- **Navigation**: Users can navigate to each week's responses using the navigation bar.
- **Password Reset**: Users can reset their passwords securely.
- **Security**: Measures are implemented to prevent SQL injection attacks.

## File Structure
- **static**: Contains images and CSS files.
  - discuss.png: Website icon.
  - style.css: Basic styling.
- **templates**: Contains HTML templates.
  - apology.html: Renders an apology when an error occurs.
  - discuss.html: Renders responses for each week.
  - index.html: Root directory displaying the difficulty of each week.
  - login.html: User login form.
  - register.html: User registration form.
  - reset.html: Password reset form.
  - response.html: Displays responses.
- **app.py**: Main application file containing route functions.
- **helpers.py**: Contains helper functions.
  - apology(): Renders an apology.
  - login_required(): Checks if the user is logged in.

## Installation
1. Clone the repository: `git clone https://github.com/Hamza-Nayab/discuss50.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `flask initdb`
4. Run the application: `flask run`

## Usage
1. Sign up or log in with your credentials.
2. Provide responses for each week of the CS50 bootcamp.
3. View and discuss responses provided by other users.
4. Navigate through weeks using the navigation bar.
5. Reset your password if needed.

## Contribution
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## About the Developer
Hamza Nayab developed Discuss 50.
