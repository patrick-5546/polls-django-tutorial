# polls-django-tutorial

Follow along with the official django tutorial for version 3.1, parts 1-7; [Part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/). I wrote some additional comments explaining certain files.

## Setup and Run Instructions

1. Install the required packages

   ```sh
   pip install -r requirements.txt
   ```

2. Create the database

   ```sh
   python manage.py migrate
   ```

3. Create an admin account

   ```sh
   python manage.py createsuperuser
   ```

4. Run the application

   ```sh
   python manage.py runserver
   ```

5. Login to the admin page and create some polls: `http://127.0.0.1:8000/admin/polls/question/add/`

6. View available polls: `http://127.0.0.1:8000/polls/`
