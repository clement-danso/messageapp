from django.db import models

# Create your models here.
class region(models.Model):
	regionName = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.regionName
	
class district(models.Model):
	districtName = models.CharField(max_length= 50)
	region = models.ForeignKey(region, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.districtName
	
class subdistrict(models.Model):
	subdistrictName = models.CharField(max_length=50)
	district = models.ForeignKey(district, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.subdistrictName
	
class bmc(models.Model):
	bmcName = models.CharField(max_length=50)
	subdistrict = models.ForeignKey(subdistrict, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.bmcName
	
class grade(models.Model):
	grade = models.CharField(max_length=50)
	
	def __str__(self):
		return self.grade
	
class group(models.Model):
	
	groupName = models.CharField(max_length=50)
	
	def __str__(self):
		return self.groupName


	
class unit(models.Model):
	unit = models.CharField(max_length=50)
	
	def __str__(self):
		return self.unit
	
class records(models.Model):
	GENDER = (
			 ('Male', 'Male'),
			 ('Female', 'Female'),
			
			 )
	TITLE = (
			 ('Mr.', 'Mr.'),
			 ('Mrs.', 'Mrs.'),
			 ('Miss.', 'Mrs.'),
			 ('Dr.', 'Dr.'),
			
			 )
			 		 
	MARITAL_STATUS = (
			 ('Single', 'Single'),
			 ('Married', 'Married'),
			 ('Divorced', 'Divorced'),
			 ('Widowed', 'Widowed'),
			
			 )
			 
	RELIGION = (
			 ('Christian', 'Christian'),
			 ('Muslim', 'Muslim'),
			 ('Other', 'Other'),
			
			 )
			 
	STATUS = (
			 ('Active', 'Active'),
			 ('Inactive', 'Inactive'),
			
			 )
	
	EmpNumber = models.CharField(max_length=11,primary_key=True)
	Title = models.CharField(max_length=11, choices=TITLE, default=TITLE[0][0])
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	OtherName = models.CharField(max_length=50)
	Gender = models.CharField(max_length=10, choices=GENDER)
	DOB = models.DateField()
	MaritalStatus = models.CharField(max_length=10, choices=MARITAL_STATUS)
	Religion = models.CharField(max_length=10, choices=RELIGION)
	OfficialEmail= models.CharField(max_length=50, unique=True)
	PersonalEmail= models.CharField(max_length=50, unique=True)
	Mobile = models.CharField(max_length=10, unique=True)
	Mobile1 = models.CharField(max_length=10, unique=True)
	FirstAppDate = models.DateField()
	AssumptionDutyDate= models.DateField()
	bmc = models.ForeignKey(bmc, null=True, on_delete=models.SET_NULL)
	unit = models.ForeignKey(unit, null=True, on_delete=models.SET_NULL)
	grade = models.ForeignKey(grade, null=True, on_delete=models.SET_NULL)
	group = models.ForeignKey(group, null=True, on_delete=models.SET_NULL)
	status = models.CharField(max_length=10, choices=STATUS, default=STATUS[0][0])
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural = 'records'
	
	def __str__(self):
		return self.FirstName



class broadcastmessage(models.Model):
	Subject=models.CharField(max_length=50)
	Content=models.CharField(max_length=400)
	Group = models.ForeignKey(group, null=True, on_delete=models.SET_NULL)
	
	class Meta:
		verbose_name_plural='Broadcast Messages'
	
	def __str__(self):
		return self.Title

class delivery(models.Model):
	sms_status = models.CharField(max_length=50)
	smstype = models.CharField(max_length=50)
	total_sent = models.CharField(max_length=50)
	total_rejected = models.CharField(max_length=50)
	recipient=models.CharField(max_length=50)
	credit_used = models.CharField(max_length=50)
	credit_left = models.CharField(max_length=50)
	date_created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'Deliveries'
	
	def __str__(self):
		return self.sms_status
