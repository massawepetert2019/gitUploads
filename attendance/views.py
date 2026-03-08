from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Meeting,Members_attendanceTb
from members.models import MembersInfo

# Create your views here.
def homePage(request):
	met=Meeting.objects.order_by('-meetId').first()
	members=MembersInfo.objects.all()
	context={
	'met_info':met,
	'members':members
	}
	return render(request,'layout.html',context)
	# return HttpResponse('welcome to Homepage')
def take_attendance(request):
	if request.method=="POST":
		# return render(request,'view.html')
		memberID=request.POST.get('memberID')
		Ruhusa=request.POST.get('Ruhusa')
		if Ruhusa =='yes':
			status='Ruhusa'
		else:
			status='Attend'
		mtoaTaarifa=request.POST.get('mtoataarifa')
		kikao=request.POST.get('meetId')
		#chake if alread exist=========
		chake=Members_attendanceTb.objects.filter(meetId=kikao, memberID=memberID)
		d=len(chake)
		if (d==0):
			attend=Members_attendanceTb.objects.create(
				meetId=kikao,
				memberID=memberID,
				Ruhusa=Ruhusa,
				mtoaTaarifa=mtoaTaarifa,
				status=status
				)
			return JsonResponse({'status':'Success'})

		else:
			msg='Tayari Umesha Tuma Taarifa Zako'
			return JsonResponse({'error':msg})
			
	

