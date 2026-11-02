# Rita Khadka portfolio: Django API + React

Folders:
- `api/`  Django REST API. Holds all your portfolio text and the contact form.
- `web/`  React page (Vite). Shows the data from the API.

You need TWO Command Prompt windows, one for each folder.

## Window 1: api (Django)
```
cd rita-portfolio\api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py createsuperuser
python manage.py runserver
```
Edit your text in `api\profile_app\management\commands\seed.py` and run `python manage.py seed` again,
or edit it at http://127.0.0.1:8000/admin/ . Text in [square brackets] shows highlighted on the page.

## Window 2: web (React)
```
cd rita-portfolio\web
npm install
npm run dev
```
Open http://localhost:5173

## Get contact messages in your email (Gmail)
Messages are always saved in /admin. To also get them by email, in the api window set these first:
```
set EMAIL_HOST_USER=youraddress@gmail.com
set EMAIL_HOST_PASSWORD=your-16-letter-app-password
set CONTACT_RECEIVER=youraddress@gmail.com
python manage.py runserver
```
Use a Gmail App Password (Google Account > Security > App passwords), never your normal password.

## API
- `GET  /api/portfolio/`  everything the page shows
- `POST /api/contact/`    `{ "name", "email", "message" }`
