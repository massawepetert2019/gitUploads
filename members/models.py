from django.db import models

# Create your models here.
class MembersInfo(models.Model):
	memberID=models.CharField(max_length=20, primary_key=True)
	fullname =models.CharField(max_length=60)
	Role=models.CharField(max_length=15)
	phone=models.CharField(max_length=20)
	gender=models.CharField(max_length=6,null=True)


	
	
class LoginTb(models.Model):
	username=models.CharField(max_length=20)
	pwd =models.CharField(max_length=255)
	status=models.IntegerField(default=0)
	

