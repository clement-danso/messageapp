from django import forms  
from smsapp.models import records, group, broadcastmessage


class RecordsForm(forms.ModelForm):
	class Meta:
		model = records
		fields = '__all__'
		
		widgets = {
            'EmpNumber': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'Enter employment number'}),
            'Title': forms.Select (attrs={'class': 'form-control'}),
            'FirstName': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'First Name'}),
            'LastName': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'OtherName': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'Other Name'}),
            'Gender': forms.Select (attrs={'class': 'form-control'}),
            'DOB': forms.DateInput (format=('%m/%d/%Y'), attrs={'type':'date', 'class': 'form-control'}),
            'MaritalStatus': forms.Select (attrs={'class': 'form-control'}),
            'Religion': forms.Select (attrs={'class': 'form-control'}),
            'OfficialEmail': forms.EmailInput (attrs={'type':'email', 'class': 'form-control', 'placeholder':'Eg: joe@email.com'}),
            'PersonalEmail': forms.EmailInput (attrs={'class': 'form-control', 'placeholder':'Eg: joe@email.com'}),
            'Mobile': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'10 digits number', 'title':'Must be 10 digits only', 'pattern':'\d{10}'}),
            'Mobile1': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'10 digits number'}),
            'FirstAppDate': forms.TextInput (attrs={'type':'date', 'class': 'form-control'}),
            'AssumptionDutyDate': forms.TextInput (attrs={'type':'date', 'class': 'form-control'}),
            'bmc': forms.Select (attrs={'class': 'form-control'}),
            'unit': forms.Select (attrs={'class': 'form-control'}),
            'grade': forms.Select (attrs={'class': 'form-control'}),
            'group': forms.Select (attrs={'class': 'form-control'}),
            'status': forms.Select (attrs={'class': 'form-control'}),
            
        }
        
class BroadcastmessageForm(forms.ModelForm):
	class Meta:
		model = broadcastmessage
		fields = '__all__'
		
		widgets = {
			'Subject': forms.TextInput (attrs={'class': 'form-control', 'placeholder':'Eg: Pin Renewal'}),
			'Content': forms.Textarea (attrs={'class': 'form-control', "rows":5, 'placeholder':'Enter the content of your message here'}),
            'Group': forms.Select (attrs={'class': 'form-control'}),
        
            
        }
        

class GroupForm(forms.ModelForm):
	class Meta:
		model = group
		fields = '__all__'
		
		widgets = {
            'groupName': forms.TextInput (attrs={'class': 'form-control'}),
        
        }
