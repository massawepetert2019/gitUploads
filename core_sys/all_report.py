from django.http import HttpResponse
from django.db import connection
from attendance.models import Members_attendanceTb,Meeting
from members.models import MembersInfo
from fpdf import FPDF
from collections import defaultdict
from datetime import date


def attendance_report(request):
	class MyPDF(FPDF):

		def header(self):
			self.set_font('Times', 'B', 11) 
			
		
			self.cell(0, 8,"MAHUDHURIO YA VIKAO VYA UWAKASI MWAKA 2026",0,0,"C")
			self.ln(5)
			self.set_fill_color(0, 128, 0)
			X=10
			Y=pdf.get_y()+5
			self.set_xy(X,Y)
			self.cell(5,5,"",1,0,"C", fill=True)
			X=X+10
			self.set_xy(X,Y)
			self.cell(20,5,"-Walio Hudhuria",0,0,"C")
			X=X+25
			self.set_xy(X,Y)
			self.set_fill_color(255, 255, 0)
			self.cell(5,5,"",1,0,"C", fill=True)
			X=X+5
			self.set_xy(X,Y)
			self.cell(20,5,"-Ruhusa",0,0,"C")
			X=X+25
			self.set_xy(X,Y)
			self.set_fill_color(255, 0, 0)
			self.cell(5,5,"",1,0,"C", fill=True)
			X=X+12
			self.set_xy(X,Y)
			self.cell(20,5,"-Hawaja Hudhuria",0,0,"C")

			self.ln(10)
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
					self.cell(20,5,f'{mdate}',border=1)			
			self.ln()
			# self.cell(0, 8, f'FROM {ldate} TO  {lydate}' , 0, 0, 'C')
			
			self.set_font('Times', 'B', 7)
		def footer(self):
			tdate=date.today()
			self.set_y(-15)
			self.set_font("Arial","I",8)
			self.cell(0,10,f'Page {self.page_no()} Mfumo wa Mahudhurio ya Vikao, Printed Date {tdate}',0,0,"C")

	pdf=MyPDF('L','mm','A4')
	pdf.add_page()
	pdf.set_font('Arial',size=12)
	#get all members details
	members = MembersInfo.objects.all()
	# Get all meetings
	vikao = Meeting.objects.all()

	# Get all attendance records once
	attendance_data = defaultdict(dict)

	with connection.cursor() as cursor:
	    cursor.execute("""
	        SELECT memberID, meetId, status
	        FROM attendance_Members_attendanceTb
	    """)
	    ddm=cursor.fetchall()
	    # for d in ddm:
	    # 	print(d)
	    
	    # for memberID, meetId, status in cursor.fetchall():
	    #     attendance_data[memberID][meetId] = status
	i = 1

	# print(attendance_data)
	for member in members:
	    uid = member.memberID
	    fname = member.fullname
	    pdf.cell(10, 7, f'{i}', 1, 0, "C")
	    pdf.cell(90, 7, f'{fname}', 1, 0)

	    for kikao in vikao:
	        meetId = kikao.meetId
	        with connection.cursor() as cursor:
	        	cursor.execute("SELECT Ruhusa, status FROM attendance_Members_attendanceTb WHERE memberID=%s AND meetId=%s",[uid,meetId])
	        	rec = cursor.fetchone()
	        	if rec:
	        		ruhusa = rec[1]
	        		if ruhusa=='Attend':
	        			pdf.set_fill_color(0, 128, 0)
	        			pdf.cell(20, 7, '', 1, 0,fill=True)
	        		elif ruhusa=='Ruhusa':
	        			pdf.set_fill_color(255, 255, 0)
	        			pdf.cell(20, 7, '', 1, 0,fill=True)
	        			
	        		
	        	else:
	        		pdf.set_fill_color(255,0, 0)
	        		pdf.cell(20, 7, '', 1, 0,fill=True)    	


	        # pdf.cell(25, 10, ruhs if ruhs else 'NIT', 1, 0)

	    pdf.ln()
	    i += 1
		

	#return pdf as responce
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='inline;filename="MAHUDHURIO_YA_VIKAO_VYA_UWAKASI_2026.pdf"'
	response.write(pdf.output(dest='S').encode('latin-1'))
	return response