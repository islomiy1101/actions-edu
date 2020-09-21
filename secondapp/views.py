from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from secondapp.models import PartQuestion,Contact_Us, Category, register_table, Question, answer_question
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

#  Home template uchun


def home(request):
    if 'user_id' in request.COOKIES:
        uid = request.COOKIES['user_id']
        usr = get_object_or_404(User, id=uid)
        login(request, usr)
        if usr.is_superuser:
            return HttpResponseRedirect('/admin')
        if usr.is_active:
            return HttpResponseRedirect('/student_dashboard')
    recent = Contact_Us.objects.all().order_by('-id')[:5]
    cats = Category.objects.all().order_by('cat_name')
    context = {'msg': recent, 'category': cats}
    return render(request, 'home.html', context)

#  About template uchun


def aboutpage(request):
    cats = Category.objects.all().order_by('cat_name')
    context = {'category': cats}
    return render(request, 'about.html', context)

# Contact_Page template uchun


def contactpage(request):

    # Nomi buyicha sartirovka qilib bitta ozgaruvchiga olish
    cats = Category.objects.all().order_by('cat_name')

    # bazadagi malumotlarni bitta ozgaruvchiga ozlashtrib templatega junatish

    all_data = Contact_Us.objects.all().order_by('-id')

   # Post qilib malumotlarni bazaga saqlash
    if request.method == 'POST':

        # post orqali jonatilvotgan qiymatlarni ozgaruvchilarga ozlashtirish
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact_Us(name=name, contact_number=contact,
                          email=email, subject=subject, message=message)  # Bazadagi tablelar nomini bizadagi yani post dagi qiymatlarni tenglash
        data.save()  # post orqali junatilvotgan qiymatlarni bazaga saqlash

        res = f"Hurmatli {name} Fikringiz uchun katta rahmat 😊"
        return render(request, "contact.html", {'status': res, 'messages': all_data, 'category': cats})

    return render(request, 'contact.html', {'messages': all_data, 'category': cats})


# Ruyxatdan otish qismi uchun Post orqali bazaga yuklash

def register(request):
    if request.method == 'POST':       # post orqali jonatilvotgan qiymatlarni ozgaruvchilarga ozlashtirish
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gtype']
        birth = request.POST['birth']
        uname = request.POST['uname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        cnumber = request.POST['pnumber']
        st = request.POST['state']
        prov = request.POST['province']
        ct = request.POST['district']
        tp = request.POST['utype']

        # if password1==password2:

        # Bazadagi tablelar nomini bizadagi yani post dagi qiymatlarni tenglash
        usr = User.objects.create_user(uname, email, password1)
        usr.first_name = fname
        usr.last_name = lname
        if tp == 'stu':
            usr.is_staff = True
        usr.save()
        usr.sert_id = "%05i" % (usr.id,)
        usr.save()

        reg = register_table(user=usr, gender=gender, dateofbirth=birth,
                             contact_number=cnumber, state=st, provin=prov, city=ct)
        # Bazadagi tablelar nomini bizadagi yani post dagi qiymatlarni tenglash
        reg.sert_id = "%05i" % (usr.id,)
        reg.save()  # post orqali junatilvotgan qiymatlarni bazaga saqlash

        return render(request, 'register.html', {'status': 'Tabriklaymiz! Hurmatli , {} Siz ro`yxatdan muvaffaqiyatli o`tdingiz'.format(fname)})
        # else:
        # messages.info(request, 'Password not matching')
        # return render(request,'register.html')

    return render(request, 'register.html')


# Login qismi uchun username va passwordni bazadagi malumotlar bn solishtirish
def check_user(request):
    if request.method == 'GET':
        un = request.GET['usern']
        check = User.objects.filter(username=un)
        if len(check) == 1:
            return HttpResponse('Exists')
        else:
            return HttpResponse('No exists')


def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['password']

        user = authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            else:
                res = HttpResponseRedirect('/student_dash')
                if 'rememberme' in request.POST:
                    res.set_cookie('user__id', user.id)
                    res.set_cookie('date_login', datetime.now())
                return res
            # if user.is_active:
            #     return HttpResponseRedirect('/teacher_dash')
        else:
            return render(request, 'home.html', {'status': 'Foydaluvchi nomi yoki paroli xato'})

    return HttpResponse('called')


@login_required
def student_dash(request):
    data = register_table.objects.get(user__id=request.user.id)
    return render(request, 'student_dashboard.html', {'data': data})


@login_required
def teacher_dash(request):
    return render(request, 'teacher_dashboard.html')


@login_required
def user_logout(request):
    logout(request)
    res= HttpResponseRedirect('/')
    res.delete_cookie('user_id')
    res.delete_cookie('date_login')
    return res
def edit_profile(request):
    context = {}
    data = register_table.objects.get(user__id=request.user.id)
    context = {'data': data}
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        con = request.POST['contact']
        ct = request.POST['city']
        gen = request.POST['gender']
        occ = request.POST['occ']
        abt = request.POST['about']

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        data.contact_number = con
        data.city = ct
        data.gender = gen
        data.occupation = occ
        data.about = abt

        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()

        context['status'] = 'O`zgarishlar muvaffaqiyatli saqlandi'
    return render(request, 'edit_profile.html', context)


@login_required
def exam_page(request):
    data = Question.objects.all().order_by('partquestion_id')
    datapart=PartQuestion.objects.all().order_by('id')
    context = {'data': data,'datapart':datapart}
    if request.method == 'POST':
        user = request.user
        for item in data:
            res = request.POST[f'optradio{item.id}']
    
            result = answer_question.objects.create(
                ansa=res, question_id_id=item.id, user_id=user)
    
            result.save()
    return render(request, 'exam.html', context)


@login_required
def change_password(request):
    context = {}
    ch = register_table.objects.filter(user__id=request.user.id)
    if len(ch) > 0:
        data = register_table.objects.get(user__id=request.user.id)
        context = {'data': data}
    if request.method == 'POST':
        current = request.POST['cpwd']
        newpass = request.POST['npwd']

        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
            user.set_password(newpass)
            user.save()
            context['msz'] = 'Parol muvaffaqiyatli yangilandi!!!'
            context['col'] = 'alert alert-success'
            user = User.objects.get(username=un)
            login(request, user)
        else:
            context['msz'] = 'Amaldagi Parol Xato'
            context['col'] = 'alert alert-danger'
    return render(request, 'change_password.html', context)

