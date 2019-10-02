from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from pipenv.vendor.tomlkit.items import Item
import datetime
from django.core.mail import send_mail
from .models import Registration, Feedback, BranchInfo, CommentData, Like_Activity,online
from .forms import RegistrationForm, Login
from django.http.response import HttpResponse

lform = None
# lform2 = None
fform = None
cform=None
user = 0

def home(request):
    return render(request, "home.html")


def Reg_View(request):
    if request.method == "POST":
        name1 = request.POST.get("name1")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        branch = request.POST.get("branch")
        batch = request.POST.get("batch")
        roll = request.POST.get("roll")

        data = Registration(
            name=name1,
            email=email,
            username=username,
            password=password,
            branch=branch,
            batch=batch,
            roll=roll
        )

        data.save()
        return render(request, "home.html")

    else:
        return render(request, "home.html")


def Login_View(request):
    if request.method == "POST":
        username1 = request.POST.get("username")
        password1 = request.POST.get("password")

        user1 = Registration.objects.filter(username=username1)
        pwd1 = Registration.objects.filter(password=password1)
        global lform
        global lform2
        lform = Registration.objects.all()
        lform2 = Registration.objects.filter(username=username1, password=password1)
        if user1 and pwd1:
            request.session.set_test_cookie()
            y = ''
            for i in lform2:
                y = i.name
            request.session['Active'] = y
            data=online(Active_member=y)
            data.save()
            return redirect(login)

        else:
            if request.method == "POST":
                name1 = request.POST.get("name1")
                email = request.POST.get("email")
                username = request.POST.get("username")
                password = request.POST.get("password")
                branch = request.POST.get("branch")
                batch = request.POST.get("batch")
                roll = request.POST.get("roll")

                data = Registration(
                    name=name1,
                    email=email,
                    username=username,
                    password=password,
                    branch=branch,
                    batch=batch,
                    roll=roll
                )

                data.save()
                return render(request, "home.html")

            else:
                return render(request, "home.html")
    else:
        return render(request, 'home.html')


def library(request):
    if request.session.get('Active'):
        return render(request, 'Lib.html')
    else:
        return render(request, 'home.html')


def logout(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session['Active']
        return redirect('/#/')


def login(request):
    if request.session.test_cookie_worked():
        request.session.set_expiry(60)

        if request.method == "POST":
            global lform2
            global x
            x = datetime.datetime.now()
            t1 = request.POST.get("t1")
            img=request.FILES.get('image')
            y=''
            for i in lform2:
                y = i.name
            data1 = Feedback(t1=t1, date=x, name=y,image=img,like=0)
            data1.save()
            
            global fform
            fform = Feedback.objects.all()
            cform = CommentData.objects.all()
            online_members=online.objects.all()
            return render(request, 'hi.html', {'lform': lform, 'lform2': lform2, 'fform': fform,'cform': cform,'online_members':online_members})
        else:
            fform = Feedback.objects.all()
            cform = CommentData.objects.all()
            online_members = online.objects.all()
            return render(request, 'hi.html', {'lform': lform, 'lform2': lform2,'fform': fform,'cform': cform,'online_members':online_members})

    else:
        y = ''
        for i in lform2:
            y = i.name
        fetch = online.objects.filter(Active_member=y)
        fetch.delete()
        return HttpResponse('<center><h1>INVALID SESSION<h1></center>')


def action(request):
    z = request.POST.get('event')
    return HttpResponse('comment not working')


def like(request,date_recieved,name_recieved):
    check_Activity=Like_Activity.objects.filter(date_of_like=date_recieved,user_like=name_recieved)
    if check_Activity:
        for c in check_Activity:
            if c.active==1:
                check_Activity.update(active=0)
                like=Feedback.objects.filter(date=date_recieved)
                for l in like:
                    like2 = l.like - 1
                    like.update(like=like2)
            else:
                check_Activity.update(active=1)
                like = Feedback.objects.filter(date=date_recieved)
                for l in like:
                    like2 = l.like + 1
                    like.update(like=like2)
    else:
        data_like=Like_Activity(
        date_of_like=date_recieved,
        user_like=name_recieved,
        active=1
         )
        data_like.save()
        like = Feedback.objects.filter(date=date_recieved)
        for l in like:
            like2 = l.like + 1
            like.update(like=like2)
    fform = Feedback.objects.all()
    cform = CommentData.objects.all()
    return render(request, 'hi.html', {'cform': cform, 'lform': lform, 'lform2': lform2, 'fform': fform})


def comment(request, date_recieved, name_recieved):
    match = Feedback.objects.filter(date=date_recieved)
    comment_date = datetime.datetime.now()
    if match:
        feedback_id = Feedback.objects.filter(date=date_recieved).values_list('id', flat=True)
        comment_name = name_recieved
        comment_text = request.POST.get("comment_text")
        comment_data = CommentData(feedback_id=feedback_id[0], comment_name=comment_name, comment_text=comment_text,
                                   comment_date=comment_date)
        comment_data.save()
        global cform
        cform = CommentData.objects.all()
    fform = Feedback.objects.all()
    cform = CommentData.objects.all()
    return render(request, 'hi.html',
                  {'lform': lform, 'lform2': lform2, 'fform': fform, 'cform': cform, 'comment_date': comment_date})


def branch_info(request):
    facultyInfo = BranchInfo.objects.all()
    return render(request, 'branch_info.html', {'faculyInfo': facultyInfo})


def reset_password(request):
    return render(request, 'reset.html')


def sendmail(request):
    import random
    global user
    user=random.randint(99999, 99999999)
    uname=request.POST.get('uname')
    email=request.POST.get('reg_email')
    pswd = request.POST.get('pswd')
    cpswd = request.POST.get('cpswd')
    validt=Registration.objects.filter(username=uname,email=email)
    if validt:
        send_mail(
        'Password Reset',
        'ka haal ba',
        'settings.EMAIL_HOST_USER',
        ['raavi277@gmail.com'],
        html_message=render_to_string('reset_conform.html', {'user': user,'uname':uname,'email':email}),
        fail_silently=False,
        )
        return render(request,'final_reset.html',{'user':user,'uname':uname})
    else:
        return HttpResponse('You have entered wrong details')

def newPassword(request,otp_recieved,user_name):
    otp=request.POST.get('otp')
    pswd=request.POST.get('pswd')
    cpswd=request.POST.get('cpswd')
    if int(otp)==int(otp_recieved):
        if pswd==cpswd:
            change_pass=Registration.objects.filter(username=user_name)
            if change_pass:
                change_pass.update(password=pswd)
                return HttpResponse('Password Changed')
            else:
                return HttpResponse('password cant be changed')
        else:
            return HttpResponse('password did not matched')
    else:
        return HttpResponse('invalid otp')

def upload_img(request):
    return HttpResponse('upload')


def active_member(request):
    return render(request,'active_member.html')