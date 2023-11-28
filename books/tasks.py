from library.celery import app
from django.core.mail import send_mail

# Отправление письма с помощью celery
@app.task
def send_test_message(person_mail):
    send_mail('Добро пожаловать!', 
              'Добрый день, спасибо за регистрацию в нашей библиотеке!', 
              'test.maksim99@gmail.com', 
              [person_mail]
            )