# Student Management System

A collaborative student management platform developed with Django (backend) and HTML/CSS/JavaScript (frontend). The system is designed to manage student records, subjects, and academic performance (activities, quizzes, and exams) using a RESTful API for seamless communication between the backend and frontend.

## Features

### User Management

- Role-based access control (Admin, Staff)
- Secure authentication with session or token-based login
- Profile and credential management

### Student Records

- Add, edit, and delete student profiles
- Assign subjects to students
- Track student grades for:
  - Activities
  - Quizzes
  - Exams

### Subject & Grade Management

- Create and manage subjects
- Record and update grades by category
- Filter and sort grades by subject, student, or score range
- Export reports (CSV or PDF support planned)

### Admin Dashboard

- Overview of student performance
- User and subject management
- Filterable tables and charts (planned)

### Staff Features

- Add/update student records
- Assign and evaluate student performance
- Secure access to academic records

## Installation

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd student-management-system
    ```

2. Create and activate virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create `.env` file:

    ```bash
    cp .env.example .env
    # Edit .env with your settings
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. Run development server:

    ```bash
    python manage.py runserver
    ```


## Frontend Setup
The frontend is a standalone HTML/CSS/JavaScript application that consumes the backend API.

Connect via API endpoints (/api/...)

Configure base URLs in frontend JS files

Optional: Use a build tool like Vite or Webpack if planning to scale

## Project Structure

```plaintext
student_management/
├── students/           # Student record app
├── subjects/           # Subject and grade app
├── users/              # Authentication and user roles
├── api/                # RESTful API integration
├── templates/          # Frontend templates
├── static/             # CSS, JS, images
└── student_management/ # Project configuration and settings
```

## Development
- Python 3.10+

- Django 5.2

- SQLite (for development)

- Django REST Framework

## Security
- Environment variables for sensitive settings

- Encrypted password storage

- CSRF protection

- Input validation and sanitization

## Contributing
1. Fork the repository

2. Create your feature branch: git checkout -b feature/your-feature

3. Commit your changes: git commit -m 'Add some feature'

4. Push to the branch: git push origin feature/your-feature

5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.


