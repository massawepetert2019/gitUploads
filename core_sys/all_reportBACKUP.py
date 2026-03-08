from django.http import HttpResponse
from django.db import connection
from attendance.models import Members_attendanceTb,Meeting
from members.models import MembersInfo
from fpdf import FPDF


def attendance_report(request):
	class MyPDF(FPDF):
		def header(self):
			self.set_font('Times', 'B', 11) 
			#self.cell(120)
			#root.iconphoto(False,ig)
			# ig="database/icap.png"
			# self.image(ig,x=5,y=2,w=25,h=20)
			# # self.ln(5)
			# self.cell(0, 8, f'{fName} ', 0, 0, 'C')
			# self.ln(5)
			self.cell(0, 8,"MAHUDHURIO YA VIKAO VYA UWAKASI MWAKA 2026",0,0,"C")
			self.ln(9)
			self.cell(10,10,"SN",1,0,"C")
			self.cell(90,10,"JINA LA MWANACHAMA",1,0,"C")
			self.multi_cell(180,5,"TAREHE ZA VIKAO",1,0,"C")
			X=pdf.get_x()-197
			Y=pdf.get_y()
			self.set_xy(X,Y)
			with connection.cursor() as cursor:
				cursor.execute("select meetId,meetingdate from attendance_Meeting")
				rec = cursor.fetchall()
				
				for data in rec:	
					mdate=data[1].strftime('%d-%m-%y')
					self.cell(25,5,f'{mdate}',border=1)			
			self.ln()
			# self.cell(0, 8, f'FROM {ldate} TO  {lydate}' , 0, 0, 'C')
			
			self.set_font('Times', 'B', 7)
		def footer(self):
			self.set_y(-15)
			self.set_font("Arial","I",8)
			self.cell(0,10,f'Page {self.page_no()} Mfumo wa Mahudhurio ya Vikao',0,0,"C")

	pdf=MyPDF('L','mm','A4')
	pdf.add_page()
	pdf.set_font('Arial',size=12)
	#get all members details
	members=MembersInfo.objects.all()
	i=1

	for member in members:
		uid=member.memberID
		fname=member.fullname
		#get meeting info
		pdf.cell(10,10,f'{i}',1,0,"C")
		pdf.cell(90,10,f'{fname}',1,1)
		vikao=Meeting.objects.all()
		Y=pdf.get_y()-10
		X=pdf.get_x()
		
		
		# pdf.set_xy(dx,Y)
		for kikao in vikao:
			meetId=kikao.meetId			
			# pdf.cell(25,10,f'{meetId}',1,0)
			# pdf.set_x(dx+25)
			xx=X+100
			dx=xx
			pdf.set_xy(dx,Y)
			with connection.cursor() as cursor:
				cursor.execute('''SELECT m.memberID,a.status,k.meetId FROM members_MembersInfo m  
					 JOIN  attendance_Members_attendanceTb a ON m.memberID = a.memberID join  attendance_Meeting k on  k.meetId=a.meetId WHERE a.meetId =%s AND a.memberID= %s''',[meetId,uid])
				attend=cursor.fetchone()
				# for attend in datt:						
				if attend:
					ruhs=attend[1]
					pdf.cell(25,10,f'{ruhs}',1,0)
					dx=dx+25
					# pdf.set_x(dx+25)
				else:
					pdf.cell(25,10,f'nit',1,0)	
					dx=dx+25
				# pdf.set_x(dx+25)


					
				

		pdf.set_xy(X,Y+10)
		
		# Y=pdf.get_y()-10
		# xx=pdf.get_x()+100
		# with connection.cursor() as cursor:
		# 	cursor.execute('''SELECT attendance_Members_attendanceTb.Ruhusa FROM attendance_Members_attendanceTb WHERE attendance_Members_attendanceTb.memberID=%s''',[uid])
		# 	datt=cursor.fetchall()
		# 	for attend in datt:
		# 		ruhs=attend[0]
		# 		pdf.set_xy(xx,Y)
				# pdf.cell(25,10,f'{meetId}',1,1)

		i=i+1


	# for i in range(49):
	# 	pdf.cell(10,10,f'{i}',1,0,"C")
	# 	pdf.cell(90,10,f'Full name {i}',1,1,"C")















	#return pdf as responce
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='inline;filename="MAHUDHURIO_YA_VIKAO_VYA_UWAKASI_2026.pdf"'
	response.write(pdf.output(dest='S').encode('latin-1'))
	return response