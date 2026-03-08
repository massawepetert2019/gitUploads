from django.db import models
from members.models import MembersInfo

# Create your models here.
class Meeting(models.Model):
	meetId = models.IntegerField(primary_key=True)
	meetingdate=models.DateField()
	location=models.CharField(max_length=90)
	Meet_status=models.CharField(max_length=10,default='Active')
	DateCreated=models.DateField(auto_now_add=True)
	DateEdited=models.DateField(auto_now=True)
	MeetNo=models.IntegerField(null=True)

class Members_attendanceTb(models.Model):
	meetId=models.CharField(max_length=12)
	memberID=models.CharField(max_length=15)
	DateCreated=models.DateField(auto_now_add=True)
	Ruhusa=models.CharField(max_length=7,null=True)
	mtoaTaarifa=models.CharField(max_length=20,null=True)
	status=models.CharField(max_length=8,null=True)

	
		
	

