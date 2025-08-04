# GMU Student Survey – Django Web Application

## 🎥 Demo Video

[Click here to watch the demo](ttps://drive.google.com/file/d/1vCIu1z3-E8s1Qd9XZmaL1hNef4NIbaqR/view?usp=sharing)


This project is a Django-based web application built to collect feedback from prospective students following their campus visits to George Mason University.

It includes a custom survey form, template rendering, database integration using SQLite, and Django's admin interface for data management.

---

## Features

- Student feedback form capturing:
  - Name, contact info, address, date of visit
  - Favorite aspects of the visit
  - Source of interest in GMU
  - Likelihood of recommendation
  - Additional comments
- Form submission and data storage via Django ORM
- Admin panel to view and manage submissions
- Input validation via Django Forms
- Responsive UI with static image and styling

---

## Tech Stack

| Category     | Tools & Frameworks         |
|--------------|-----------------------------|
| Backend      | Python 3, Django            |
| Database     | SQLite (default), extensible to MySQL/PostgreSQL |
| Templates    | Django Templates (HTML/CSS) |
| Forms        | Django Forms                |
| Admin Panel  | Django Admin Interface      |


---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/jhansisneha/gmu-django-student-survey.git
cd gmu-django-student-survey
```
2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install django
```
4. **Run migrations**
```bash   
python manage.py migrate
```
5. **Start the development server**
```bash
python manage.py runserver
```
## Future Enhancements
- Add deployment to Heroku, Render, or AWS
- Switch database to PostgreSQL or MySQL
- Add REST API endpoints using Django REST Framework
- Add email notifications on form submission
- Add CSV export or analytics dashboard
