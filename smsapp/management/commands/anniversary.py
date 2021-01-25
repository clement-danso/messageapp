"""
Custom management command that sends an email to all users
born on the current day and month.
"""
import requests
import json

from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
#from someplace import User
from smsapp.models import records, delivery


class Command(BaseCommand):
	def handle(self, **options):
		today = timezone.now().date()
		for record in records.objects.filter(FirstAppDate__day=today.day, FirstAppDate__month=today.month):
			#subject = 'Happy birthday %s!' % records.FirstName
			#body = 'Hi %s,\n...' + user.first_name
			#send_mail(subject, body, 'contact@yourdomain.com', [user.email])
			
			endPoint = 'https://api.mnotify.com/api/sms/quick'
			apiKey = 'ZUO6WljHntroazsSTNz7MMJ2EJZ3CjfBe4Iap1SNujbFT'
			data = {
			   'recipient[]': [record.Mobile],
			   'sender': 'Quoda',
			   'message': 'Good morning. Happy work anniversary %s!' % record.FirstName,
			   'is_schedule': False,
			   'schedule_date': ''
			}
			url = endPoint + '?key=' + apiKey
			response = requests.post(url, data)
			data = response.json()
			
			bstatus=json.dumps(data['status'])
			bsmstype='Anniversary'
			btotalsent=json.dumps(data["summary"]["total_sent"])
			btotalrejected=json.dumps(data["summary"]["total_rejected"])
			brecipient=json.dumps(data["summary"]["numbers_sent"])
			bcreditused=json.dumps(data["summary"]["credit_used"])
			bcreditleft=json.dumps(data["summary"]["credit_left"])
			
			delivery_instance = delivery(
										sms_status=bstatus, 
										smstype=bsmstype, 
										total_sent=btotalsent, 
										total_rejected=btotalrejected, 
										recipient=brecipient, 
										credit_used=bcreditused, 
										credit_left=bcreditleft
										)
			delivery_instance.save()
