from django.shortcuts import render,redirect
from busroutings.models import Studentinfo, BusInfo

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    clgid = request.POST.get('clgid')
    pswd = request.POST.get('pass')
    ob = Studentinfo.objects.filter(collegeid = clgid, password = pswd)

    if ob:
        x=[]
        for i in ob:
            x.append(i.collegeid)
            x.append(i.name)
            x.append(i.branch)
            x.append(i.collegename)
            x.append(i.year)
            x.append(i.contact)
            x.append(i.emailid)
            x.append(i.boardingpt)
            x.append(i.busno)
            ob1 = BusInfo.objects.filter(busNo = i.busno)
            for j in ob1:
                x.append(j.driverName)
                x.append(j.driverContact)
                x.append(j.busRoute)
        return render(request, 'dashboard.html', {'key':x})
    else:
        return redirect('/')