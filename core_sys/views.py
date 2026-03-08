from django.shortcuts import render
from members.models import MembersInfo
from attendance.models import Members_attendanceTb,Meeting
from .all_report import attendance_report
#,Meeting
from django.db import connection

# Create your views here.
def dashbord(request):
	return render(request,'dashbord_layout.html')

def about(request):
	return render(request,'about.html')

def memberPage(request):
	members=MembersInfo.objects.all()
	return render(request,'members.html',{'members':members})

def attendancePage(request):
	#memberID,Meeting.meetId,meetingdate,#Members_attendanceTb.meetId,memberID,Ruhusa==attendance_Meeting.meetingdate,MeetNo attendance_Meeting.MeetNo,
	with connection.cursor() as cursor:
		cursor.execute('''SELECT attendance_Meeting.meetingdate,members_MembersInfo.fullname,members_MembersInfo.Role,attendance_Members_attendanceTb.status,attendance_Meeting.MeetNo,
			attendance_Members_attendanceTb.Ruhusa from members_MembersInfo,attendance_Meeting inner join attendance_Members_attendanceTb on 
			attendance_Members_attendanceTb.memberID=members_MembersInfo.memberID group by attendance_Members_attendanceTb.meetId,attendance_Members_attendanceTb.memberID''')
		rec=cursor.fetchall()
		#convert list to dictionary and send it 
	members=[]
	for row in rec:
		members.append({
			'uid':row[0],
			'fulname':row[1],
			'role':row[2],
			'status':row[3],
			'kikaoDate':row[4],
			})

	# members=MembersInfo.objects.all()
	return render(request,'attendance.html',{'members':members})

def reportPage(request):
	members=MembersInfo.objects.all()
	vikao=Meeting.objects.all()
	return render(request,'report.html',{'members':members,'vikao':vikao})

def download_kikao(request):
	attendance_report(request)

