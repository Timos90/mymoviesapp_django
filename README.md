# MyMoviesApp 🎬

A Django-based web application for managing movies, including user interactions such as ratings, reviews, and watchlists. This project uses Django's built-in user authentication system and connects a variety of tables like movies, deleted movies, and user-specific data.

---

## Features
- Manage a movie database with detailed metadata (title, release year, director, budget, etc.).
- User authentication using Django's default user model.
- Functionalities like adding ratings, reviews, and maintaining watchlists.
- Integration with PostgreSQL for database storage.

---

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/Timos90/mymoviesapp_django.git
cd mymoviesapp
```
### 2. Create a Virtual Environment and Install Dependencies
```bash
python3 -m venv .venv --prompt mymoviesapp
source .venv/bin/activate
pip install -r requirements.txt or make dev-install
```
### 3. Configure PostgreSQL Database
Ensure PostgreSQL is installed and running.

Create a database (e.g., `mymoviesdb`) and a `.env` file. Copy and paste the text below inside the file.

```python
SECRET_KEY=      
DB_NAME=
DB_USER=
DB_PWD=
DB_PORT=5432
DB_HOST=localhost
```
Generate a secret key and fill in the db_name, db_user and db_pwd with preferred values.
### 4. Run Database Migrations
Run the following commands to apply database migrations:

```bash
python3 manage.py makemigrations or make dev-makem
python3 manage.py migrate or make dev-m
```
### Populate the Database
Manually add movies to the database via the Django Admin interface or use the provided data in `data/movies.json`.
### Start the Development Server
Start the Django development server:
```bash
python manage.py runserver --settings=config.settings.dev or make
```
Visit the application in your browser at http://127.0.0.1:8000.