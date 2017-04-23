=========================
django-backend-activity
========================
I have created this task using Django and Django rest framework

Setup project environment
--------------------------
- run $ pyvenv <your-env-name>
- activate environment using $ source <your-env-name>/bin/activate


Install required packages
------------------------
- keeping your environment activated from the root directory of the project run $ pip install -r requirements/base.txt

Set Environment Variables
------------------------
- cd into tratolitask folder and from here run $ export DJANGO_SETTINGS_MODULE='tratolitask.settings.local'

Manually create secrets.json file
---------------------------------


Run the server
---------------
- Now you can run the server from tratolitask folder $ python manage.py runserver


APIs
---------------

**Create a Message**

 - Method : POST
 - URL: http://127.0.0.1:8000/api/v1/chat-messages/
 - headers: Content-Type: application/json
 - request_body:
     ```
     {
         "text": "Lio de vasio",
         "user_id": "1"
     }
     ```

