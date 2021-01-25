from django.shortcuts import render, redirect
from django.utils import timezone
from smsapp.models import *
from smsapp.forms import *
import requests
import json
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
	today = timezone.now().date()
	alrecods=records.objects.all()
	recods=records.objects.all().order_by('-date_created')[:5]
	deliveries=delivery.objects.all().order_by('-date_created')[:10]
	aldeliveries=delivery.objects.all()
	act_recods=records.objects.filter(status='Active')
	inact_recods=records.objects.filter(status='Inactive')
	
	bdaysms=delivery.objects.filter(smstype='Birthday').count()
	annisms=delivery.objects.filter(smstype='Anniversary').count()
	bsms=delivery.objects.filter(smstype='Broadcast').count()
	welsms=delivery.objects.filter(smstype='Welcome').count()
	
	recodsnum=alrecods.count()
	activenum=act_recods.count()
	inactivenum=inact_recods.count()
	
	context={
		'recods':recods,
		'recodsnum':recodsnum,
		'activenum':activenum, 
		'inactivenum':inactivenum, 
		'deliveries':deliveries,
		'aldeliveries':aldeliveries,
		'alrecods':alrecods,
		'bdaysms': bdaysms,
		'annisms': annisms,
		'bsms': bsms,
		'welsms': welsms,
		} 
	return render(request, 'smsapp/dashboard.html', context)


@login_required
def createrecord(request):
	"""form page for creating records"""
	fm = RecordsForm()
	if request.method == 'POST':
		fm = RecordsForm(request.POST)
		
		if fm.is_valid():
			fm.save()
		
		fon=request.POST.get('Mobile')
		titlename=request.POST.get('Title')
		firstname=request.POST.get('FirstName')
		lastname=request.POST.get('LastName')
		emaill=request.POST.get('OfficialEmail')
		dateOB=request.POST.get('DOB')
		
		
		endPoint = 'https://api.mnotify.com/api/sms/quick'
		apiKey = 'ZUO6WljHntroazsSTNz7MMJ2EJZ3CjfBe4Iap1SNujbFT'
		data = {
			   'recipient[]': fon,
			   'sender': 'Quoda',
			   'message': 'Hello %s thank you for joining GHS WN RHD' % firstname,
			   'is_schedule': False,
			   'schedule_date': ''
			}
		url = endPoint + '?key=' + apiKey
		response = requests.post(url, data)
		data = response.json()
		
		bstatus=json.dumps(data['status'])
		bsmstype='Welcome'
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
		return redirect('/home')
		
	context = {'fm':fm}
	
	return render(request, 'smsapp/recordfrm.html', context)

@login_required
def creategroup(request):
	
	fm = GroupForm()
	if request.method == 'POST':
		fm = GroupForm(request.POST)
		
		if fm.is_valid():
			fm.save()
		
		
		return redirect('/grouplist')

	context = {'fm':fm}
	return render(request, 'smsapp/groupfrm.html', context)

@login_required
def createbmessage(request):
	"""form page for creating records"""
	fm = BroadcastmessageForm()
	if request.method == 'POST':
		fm = BroadcastmessageForm(request.POST)
		grup=request.POST.get('Group')
		
		group_records=records.objects.filter(group=grup)
		
		cont=request.POST.get('Content')
		
		for recod in group_records:
			endPoint = 'https://api.mnotify.com/api/sms/quick'
			apiKey = 'ZUO6WljHntroazsSTNz7MMJ2EJZ3CjfBe4Iap1SNujbFT'
			data = {
			   'recipient[]': [recod.Mobile],
			   'sender': 'Quoda',
			   'message': cont,
			   'is_schedule': False,
			   'schedule_date': ''
			}
			url = endPoint + '?key=' + apiKey
			response = requests.post(url, data)
			data = response.json()
			
			bstatus=json.dumps(data['status'])
			bsmstype='Broadcast'
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
			
			return redirect('/home')
	
	context = {'fm':fm}
	
	return render(request, 'smsapp/bcmessagefrm.html', context)

@login_required
def messtemp(request):
	fm=MesstempForm()
	if request.method == 'POST':
		fm = MesstempForm(request.POST)
		
		
		tit=request.POST.get('Title')
		cont=request.POST.get('Content')
		
		endPoint = 'https://api.mnotify.com/api/template'
		apiKey = 'ZUO6WljHntroazsSTNz7MMJ2EJZ3CjfBe4Iap1SNujbFT'
		data = {
		   'title': tit,
		   'content': cont
		}
		url = endPoint + '?key=' + apiKey
		response = requests.post(url, data)
		data = response.json()
		
		messtemp_id=json.dumps(data["_id"])
		messtemp_instance = messagetemp(Template_id=messtemp_id, Title=tit, Content=cont)
		messtemp_instance.save()
		
		return redirect('/home')
	
	context = {'fm':fm}

	return render(request, 'smsapp/messtempfrm.html', context)

@login_required
def recordlist(request):
	recods=records.objects.all()

	
	context={'recods':recods}
	return render(request, 'smsapp/records.html', context)

@login_required
def grouplist(request):
	grps=group.objects.all()
	
	context={'grps':grps}
	return render(request, 'smsapp/groups.html', context)

@login_required	
def templatelist(request):
	temps=messagetemp.objects.all()
	
	context={'temps':temps}
	return render(request, 'smsapp/templates.html', context)


@login_required
def deliverylist(request):
	delivs=delivery.objects.all()
	
	context={'delivs':delivs}
	return render(request, 'smsapp/deliveries.html', context)
