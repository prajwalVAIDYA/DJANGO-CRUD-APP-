# Django CRUD App

This is a simple CRUD (Create, Read, Update, Delete) application built using the Django web framework.

![image](https://github.com/user-attachments/assets/fbea2e93-d266-47a2-85a4-9d968cdb7a97)


## Features

- Create new members
- View a list of all members
- Edit existing member details
- Delete members

## Requirements

- Python 3.x
- Django 5.0.7

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/django-crud-app.git

2. Navigate to the project directory:
   cd django-crud-app

3. Create a virtual environment (optional but recommended):
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

4. Apply database migrations:
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

6. Open your web browser and visit http://127.0.0.1:8000/crud/ to access the application.

## Usage
- To create a new member, click on the "Create Member" link or navigate to http://127.0.0.1:8000/crud/create/. Fill in the member details and submit the form.
- The home page (http://127.0.0.1:8000/crud/) displays a list of all members.
- To edit a member, click on the "Edit" link next to the desired member. Update the details and save the changes.
- To delete a member, click on the "Delete" link next to the desired member. Confirm the deletion.
