from genericpath import exists
from operator import gt
from django.contrib import messages
from django.forms import IntegerField
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from adminpanel.models import Participants, Viralload,Rerand,EOIC,VLMONTH6
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def home(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard/admin')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect("/")

    else:
        return render(request,'login/login.html')  
def register(request):
    if request.method =='POST':
       username=request.POST['username']
       firstname=request.POST['firstname']
       lastname=request.POST['lastname']
       email=request.POST['email']
       password=request.POST['password']
       cpassword=request.POST['cpassword']
       if password==cpassword:
            if User.objects.filter(username=username).exists():

                messages.warning(request,'The username has already been taken')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email has already been taken')
                return redirect ('register')
            else:
                user= User.objects.create_user(username=username, first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect("/")
       else: 
        messages.warning(request,'passwords do not match')
        return redirect ('register')
    else:

     return render(request,'login/register.html')
@login_required(login_url='/')
def participnats(request):
    participants=User.objects.all()
    return render(request, 'admin/pages/participants.html',{'participant': participants})

@login_required(login_url='/')
def dashboard(request):
    total_user = Participants.objects.count()
    total_eoic = EOIC.objects.count()
    total_rerand=Rerand.objects.count()
    users=User.objects.all()
    return render(request,'admin/pages/dashboard.html',{'total_participants':total_user,'user':users,'total_eoic':total_eoic,'total_rerand':total_rerand})

def logout_view(request):
    logout(request)
    return redirect("/")
    

@login_required(login_url='/')
def new_participants(request):
    if request.method =='POST':
        pid = request.POST['pid']
        age = request.POST['age']
        psex = request.POST['psex']
        enrol_date = request.POST['enrol_date']
        s_initials = request.POST['s_initials']
        
        if Participants.objects.filter(participant_id=pid).exists():
            messages.warning(request,'participant ID already exists')
            return redirect("add-participants")
        else:
            participant= Participants.objects.create(participant_id=pid,sex=psex,age=age,enrollment_date=enrol_date,staff_initials=s_initials)
            participant.save()
            messages.info(request,'Participant ha been created successfully.')
            return redirect("add-participants")


    else:
        return render(request,'admin/pages/add_participant.html')
@login_required(login_url='/')
def edit_participant(request,id):
    users = Participants.objects.get(id=id)
    if request.method =='POST':
        pid = request.POST['pid']
        age = request.POST['age']
        psex = request.POST['psex']
        enrol_date = request.POST['enrol_date']
        s_initials = request.POST['s_initials']

        if Participants.objects.filter(participant_id=pid).exists():
            messages.info(request,'particiant ID already exists.Kindly check your ID and try again.')
            return render(request,'admin/pages/edit_participant.html',{'participants': users})
            
        else: 
            Participants.objects.filter(id=id).update(participant_id=pid,sex=psex,age=age,enrollment_date=enrol_date,staff_initials=s_initials)
            messages.info(request,'Participant updated successfully')
            return redirect("new_participants")
    else:
        return render(request,'admin/pages/edit_participant.html',{'participants': users})

@login_required(login_url='/')
def delete_participant(request,id):
    users= Participants.objects.get(id=id).delete()
    messages.info(request,'Participant has been deleted successfully.')
    return redirect("new_participants")
def all_participants(request):
    users =Participants.objects.all()
    return render(request,'admin/pages/new_participants.html',{'user':users})
def view_participant(request,id):
    users = Participants.objects.get(id=id)
    return render(request,'admin/pages/show_participants.html',{'participants': users})
def viralloads(request,id):
    users = Participants.objects.get(id=id)
    vl_loads=Viralload.objects.filter(participants_id = users)
    if request.method == 'POST':
        viral_id = request.POST['viral_id']
        has_vl = request.POST['has_vl']
        vl_result = request.POST['vl_result']
        date_collected = request.POST['date_collected']
        date_received = request.POST['date_received']
        date_entered = request.POST['date_entered']
        staff_initials = request.POST['staff_initials']
        viralloads= Viralload.objects.create(participants_id=viral_id,vl_captured= has_vl,date_collection=date_collected,vl_results=vl_result,date_received=date_received
        ,date_entered=date_entered, staff_initials=staff_initials)
        viralloads.save()
        messages.success(request,'Viral load captured successfully')
        return render(request,'admin/viral/viralload.html',{'participants': users,'viralloads':vl_loads})
    else:

        return render(request,'admin/viral/viralload.html',{'participants': users,'viralloads':vl_loads})
@login_required(login_url='/')
def highvl(request):
    high_viralload=Viralload.objects.filter(vl_results__gt =1000)
    return render(request,'admin/viral/highvl.html',{'vl_high':high_viralload})
@login_required(login_url='/')
def rerandview(request,id):
    high_viralload=Viralload.objects.get(id=id)
    if request.method=='POST':
        viral_id =request.POST['viral_id']
        p_id =request.POST['p_id']
        rerand_date =request.POST['rerand_date']
        vl_results =request.POST['vl_results']
        rerand_arm =request.POST['rerand_arm']
        staff_initials =request.POST['staff_initials']
        if Rerand.objects.filter(participants_id=p_id).exists():
            messages.info(request,'This participant has alredy been rerandomized')
            return render(request,'admin/viral/view_viralload.html',{'viral_load':high_viralload})
        else:

            rerand_data=Rerand.objects.create(viralload_id=viral_id,participants_id=p_id,rerand_date=rerand_date,vl_results=vl_results
            ,rerand_arm=rerand_arm,staff_initials=staff_initials)
            rerand_data.save()
            return redirect("all_rerand")

    else:
        return render(request,'admin/viral/view_viralload.html',{'viral_load':high_viralload})
@login_required(login_url='/')
def all_rerand(request):
    rerand=Rerand.objects.all()
    return render(request,'admin/rerand/all_rerand.html',{'rerand':rerand})
@login_required(login_url='/')
def month6(request,id):
    rerand=Rerand.objects.get(id=id)
    if request.method == 'POST':
        rerand_id=request.POST['rerand_id']
        pid=request.POST['pid']
        collection_date=request.POST['collection_date']
        vl_results=request.POST['vl_results']
        vl_suppressed=request.POST['vl_suppressed']
        r_date=request.POST['r_date']
        sinitials=request.POST['sinitials']

        if VLMONTH6.objects.filter(rerand_id=id).exists():
            messages.warning(request,'Month 6 post rerandomization for this participant has already been done.')
            return render(request,'admin/month6/index.html',{'rerand':rerand})

        else:
            vlmonth6=VLMONTH6.objects.create(rerand_id=rerand_id,participants_id=pid,collection_date=collection_date
            ,vl_result=vl_results,date_received=r_date,staff_initials=sinitials,vl_suppressed=vl_suppressed)
            vlmonth6.save()
            messages.success(request, 'Month 6 post rerandomization has been captured successfully')
            return redirect("all_month6")
    else:
        return render(request,'admin/month6/index.html',{'rerand':rerand})
@login_required(login_url='/')
def allmonth6(request):
    month6=VLMONTH6.objects.all()
    return render(request,'admin/month6/all_month6.html',{'month6':month6})
@login_required(login_url='/')
def extended_outcome(request):
    viralload_id=Viralload.objects.values('participants_id')
    participants =Participants.objects.exclude(participant_id__in=viralload_id)
    return render(request,'admin/eoic/eoic.html',{'participant':participants})
@login_required(login_url='/')
def eoic_participants(request,id):
    participants_eoic= Participants.objects.get(id=id)
    if request.method =='POST':
        pid=request.POST['pid']
        vl_result=request.POST['vl_result']
        s_initials=request.POST['s_initials']
        i_date=request.POST['i_date']
        e_date=request.POST['e_date']
        if EOIC.objects.filter(eoic_id=id).exists():
            messages.warning(request,'EOIC has already been conducted for this participant.')
            return render(request,'admin/eoic/eoic_add.html',{'participants':participants_eoic})
        else:
            eoic_save= EOIC.objects.create(eoic_id=pid,vl_result=vl_result,investigation_date=i_date,entry_date=e_date,
                staff_initials=s_initials)
            eoic_save.save()
            messages.info(request,'Participants EOIC has been captured successfully.')
            return render(request,'admin/eoic/eoic_add.html',{'participants':participants_eoic})
    else:
        return render(request,'admin/eoic/eoic_add.html',{'participants':participants_eoic})
@login_required(login_url='/')
def done_eoic(request):
    eoic_part=EOIC.objects.all()
    return render(request,'admin/eoic/done_eoic.html',{'eoic_part':eoic_part})