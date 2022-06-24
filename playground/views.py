'''from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage'''
# from django.db.models import Q, F, Func, Value
# from django.db.models.aggregates import Count, Max, Min, Avg
# from django.db.models.functions import Concat
# from store.models import Product, OrderItem, Customer

from urllib.robotparser import RequestRate
from django.shortcuts import render
from .tasks import notify_customers


'''def say_hello(request):
    try:
        #send_mail('subject', 'message', 'info@oktavsell.com', ['frans@oktavsell.com']) #send plain email from normal sender
        #mail_admins('subject', 'message', html_message='message') #send email with #send plain and html email from root
        #--- this is sample using EmailMessage-------
        # message = EmailMessage('subject', 'message', 'from@oktavsell.com', ['styo@oktavsell.com'])
        # message.attach_file('playground/static/images/cat_image.jpg')
        # message.send()
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context = {'name':'Oktav'}
        )
        message.send(['styo@oktavsell.com'])
    except BadHeaderError:
        pass
    
    return render(request, 'hello.html', {'name': 'Okta'})'''

def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Okta'})