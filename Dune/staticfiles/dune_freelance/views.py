from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
import pytz
from datetime import datetime
import string
import random
def is_meneger(user):
    return user.groups.filter(name='manager').exists()



def index(request):
    return render(request, 'index.html')

def prof(request):
    return render(request, 'proff.html')


def reg(request):
    if request.method == 'POST':
        log_in = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password1')
        if password2!= password:
            error_message = 'Пароли не совпадают!'
            return render(request, 'registration.html', {'error':error_message})
        elif User.objects.filter(email=email).exists():
            error_message = 'Пользователь с таким EMAIL уже существует!'
            return render(request, 'registration.html', {'error': error_message})
        elif User.objects.filter(username=log_in).exists():
            error_message = 'Пользователь с таким LOGIN уже существует!'
            return render(request, 'registration.html', {'error': error_message})
        else:
            user = User(username = log_in, email=email, password = password)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('projects')
    return render(request, 'registration.html')

def auth(request):
    if request.method == 'POST':
        name = request.POST.get('login')
        pasword = request.POST.get('password')
        us = authenticate(request, username=name, password=pasword)
        if us:
            login(request,us)
            return redirect('projects')
        else:
            error = "Пароль или Почта не совпадают!"
            return render(request, 'auth.html', {'error':error})
    return render(request, 'auth.html')

def auth_men(request):
    if request.method == 'POST':
        name = request.POST.get('login')
        password = request.POST.get('passsword')
        uss = authenticate(request, username=name, password=password)
        if uss:
            login(request,uss)
            return redirect('projects_m')
    return render(request, 'auth_men.html')

def profile(request):
    us_infor = request.user
    us_information = {'name':us_infor.username, 'email':us_infor.email}
    return render(request, 'profile.html', {'us_information':us_information})

def blogers(request):
    if request.method == 'POST':
        photo_blog = request.FILES.get('photo')
        nickname = request.POST.get('nickname')
        telephone = request.POST.get('telephone')
        em = request.POST.get('em')
        categr = request.POST.get('categor')
        subs = request.POST.get('subs')
        summ = request.POST.get('summ')
        tem = request.POST.get('tem')
        try:
            blog = models.Bloger(user=request.user, photo_file=photo_blog, name_first=nickname, tel_num=telephone, us_email=em, social_net=categr, subs=subs, num=summ,tem=tem)
            blog.save()
            return redirect('blogers')
        except:
            error = 'Не вспе поля заполнены'
            return render(request, 'bloger.html', {'error':error})

    try:
        blog_us = models.Bloger.objects.filter(user=request.user)
    except:
        error = 'Ошибка'
        return render(request, 'bloger.html', {'error': error})
    return render(request, 'bloger.html', {'blog_us':blog_us})


def post(request):
    try:
        post = models.Posts.objects.filter(projects_post__blog__user = request.user)
    except:
        error = 'Не вспе поля заполнены'
        return render(request, 'post.html', {'error': error})

    if request.method == 'POST':
        idd = request.POST.get('idd')
        forma = request.POST.get('format')
        date_start_proj = request.POST.get('start_project')
        time_start_proj = datetime.strptime(date_start_proj, '%Y-%m-%d')
        world_proj = pytz.timezone('Europe/Minsk')
        sp = timezone.make_aware(time_start_proj, world_proj)
        date_finish_proj = request.POST.get('finish_project')
        time_finish_proj = datetime.strptime(date_finish_proj, '%Y-%m-%d')
        world_project = pytz.timezone('Europe/Minsk')
        fp = timezone.make_aware(time_finish_proj, world_project)
        url = request.POST.get('url')

        try:
            posts_p = models.Posts.objects.get(id=idd)
            posts_p.date_nach = sp
            posts_p.data_konec = fp
            posts_p.format = forma
            posts_p.work_url = url
            posts_p.kol_p +=1
            posts_p.save()
        except:
            error = 'Не вспе поля заполнены'
            return render(request, 'post.html', {'error': error})


    return render(request, 'post.html', {'p':post})

def result_b(request):
    result_b = models.Posts.objects.filter(projects_post__blog__user = request.user)
    return render(request, 'result_blog.html', {'res_b':result_b})

@login_required()
@user_passes_test(is_meneger)
def result(request):
    results = models.Posts.objects.filter(projects_post__blog__user = request.user)
    return render(request, 'result.html', {'res':results})

@login_required()
@user_passes_test(is_meneger)
def random_m(requst):
    pass_random = ''
    if requst.method == 'POST':
        password_random = string.ascii_letters + string.digits
        for rando in range(1,12):
            char = random.choice(password_random)
            pass_random+=char
    return render(requst, 'random.html', {'pr':pass_random})

@login_required()
@user_passes_test(is_meneger)
def posts_m(request):
    aplic_m_post = models.Posts.objects.filter(projects_post__blog__user = request.user)
    if request.method == 'POST':
        id_m = request.POST.get('id_m')
        format_m = request.POST.get('format_m')
        sm = request.POST.get('start_project_m')
        time_start_proj_m = datetime.strptime(sm, '%Y-%m-%d')
        world_proj_m = pytz.timezone('Europe/Minsk')
        spm = timezone.make_aware(time_start_proj_m, world_proj_m)
        fm = request.POST.get('finish_project_m')
        time_start_proj_mf = datetime.strptime(fm, '%Y-%m-%d')
        world_proj_mf = pytz.timezone('Europe/Minsk')
        fpm = timezone.make_aware(time_start_proj_mf, world_proj_mf)
        url_m = request.POST.get('url_m')
        try:
            aplic_m_p = models.Posts.objects.get(id=id_m)
            aplic_m_p.date_nach = spm
            aplic_m_p.data_konec = fpm
            aplic_m_p.format = format_m
            aplic_m_p.work_url = url_m
            aplic_m_p.kol_p += 1
            aplic_m_p.save()
        except:
            error = 'Не вспе поля заполнены'
            return render(request, 'post_m.html', {'error': error})

    return render(request, 'posts_m.html', {'apm': aplic_m_post})



@login_required()
@user_passes_test(is_meneger)
def blogers_m(request):
    if request.method == 'POST':
        photo_m = request.FILES.get('photo_m')
        nickname_m = request.POST.get('nickname_m')
        telephone_m = request.POST.get('telephone_m')
        em_m = request.POST.get('em_m')
        categr_m = request.POST.get('categor_m')
        subs_m = request.POST.get('subs_m')
        summ_m = request.POST.get('summ_m')
        tem_m = request.POST.get('tem')
        try:
            blog_m = models.Bloger(user=request.user,tem=tem_m, photo_file=photo_m, name_first=nickname_m, tel_num=telephone_m, us_email=em_m, social_net=categr_m, subs=subs_m, num=summ_m)
            blog_m.save()
            return redirect('blogers_m')
        except:
            error = 'Не вспе поля заполнены'
            return render(request, 'bloger_m.html', {'error':error})

    try:
        blog_mus = models.Bloger.objects.filter(user=request.user)
    except:
        error = 'Ошибка'
        return render(request, 'bloger_m.html', {'error': error})

    return render(request, 'bloger_m.html', {'blog_mus':blog_mus})

def admin(request):
    return render(request, 'admin.html')

def applications_b(request):
    apl_b = models.Applications.objects.filter(blog__user = request.user)
    return render(request, 'applications_b.html',{'apl_b':apl_b})



@login_required()
@user_passes_test(is_meneger)
def profile_manager(request):
    us_man = request.user
    us_man_inf = {'name':us_man.username, 'email':us_man.email}
    return render(request, 'profile_meneger.html', {'us_man_inf':us_man_inf})

@login_required()
@user_passes_test(is_meneger)
def applications(request):
    p = models.Projects_men.objects.filter(us_manager=request.user)
    ap = models.Applications.objects.filter(pr__in = p)
    if request.method == 'POST':
        id_ap = request.POST.get('id_a')
        status = request.POST.get('status')
        if status == "Принята":
            possst = models.Posts.objects.create(projects_post_id=id_ap)
        try:
            id_ap = models.Applications.objects.get(id = id_ap)
            if status:
                id_ap.applicat = status
                id_ap.save()
                return redirect('applic')
        except:
            error = 'Ошибка'
            return render(request, 'Applications.html', {'error': error})

    return render(request, 'Applications.html',{'aplicat':ap})



def bloger_info(request, bloger_id):
    try:
        bloger_inf = models.Bloger.objects.get(id=bloger_id)
    except:
        error = 'Возникла ошибка'
        return render(request, 'bloger_profile.html', {'error':error})

    return render(request, 'bloger_profile.html', {'bloger_info':bloger_inf})


@login_required()
@user_passes_test(is_meneger)
def applications_m(request):
    aplic_m = models.Applications.objects.filter(blog__user = request.user)
    return render(request, 'applic_b.html', {'aplic_m': aplic_m})


def projects(request):
    try:
        projects_blog = models.Projects_men.objects.all()
    except:
        error = 'Ошибка'
        return render(request, 'project.html', {'error':error})
    return render(request, 'project.html', {'projects_blog':projects_blog})

@login_required()
@user_passes_test(is_meneger)
def bloger_info_m(request, bloger_id):
    try:
        bloger_inf_m = models.Bloger.objects.get(id=bloger_id)
    except:
        error = 'Возникла ошибка'
        return render(request, 'bloger_profile_m.html', {'error':error})


    return render(request, 'bloger_profile_m.html', {'bloger_info_m':bloger_inf_m})

def projects_information(request,projects_id):
    try:
        projects_informations = models.Projects_men.objects.get(id=projects_id)
    except:
        error = 'Ошибка'
        return render(request, 'project_bl_info.html', {'error': error})

    try:
        proj_inf_all = models.Projects_men.objects.all()
    except:
        error = 'Ошибка'
        return render(request, 'project_bl_info.html', {'error': error})

    try:
        bl = models.Bloger.objects.filter(user=request.user)
    except:
        error = 'Ошибка'
        return render(request, 'project_bl_info.html', {'error': error})

    if request.method == 'POST':
        appl = request.POST.get('applic')
        bloger = models.Bloger.objects.get(id=appl)
        applic = models.Applications.objects.create(pr=projects_informations)
        applic.blog.add(bloger)
        applic.save()

        return redirect('projects')

    return render(request, 'project_bl_info.html',{'proj_inf':projects_informations, 'prinfal':proj_inf_all, 'bl':bl})



@login_required()
@user_passes_test(is_meneger)
def projects_info(request,projects_men_id):
    try:
        proj_inf = models.Projects_men.objects.get(id=projects_men_id)
    except:
        error = 'Ошибка'
        return render(request, 'project_info.html', {'error':error})

    try:
        proj_all = models.Projects_men.objects.all()
    except:
        error = 'Ошибка'
        return render(request, 'project_info.html', {'error': error})

    try:
        bl_m = models.Bloger.objects.filter(user=request.user)
    except:
        error = 'Ошибка'
        return render(request, 'project_info.html', {'error': error})
    if request.method == 'POST':
        id_bl = request.POST.get('id_bl')
        blogers = models.Bloger.objects.get(id=id_bl)
        applic_m = models.Applications.objects.create(pr=proj_inf)
        applic_m.blog.add(blogers)
        applic_m.save()
        return redirect('projects_m')

    return render(request, 'project_info.html', {'proji':proj_inf, 'projal':proj_all,'bl_m':bl_m})
@login_required()
@user_passes_test(is_meneger)
def projects_m(request):
    if request.method == 'POST':
        image = request.FILES.get('input_photo')
        name = request.POST.get('name_project')
        email = request.POST.get('email_men')
        number = request.POST.get('summ')
        type_social = request.POST.get('category')
        type_pay = request.POST.get('pay')
        status = request.POST.get('status')
        start = request.POST.get('start')
        time_start = datetime.strptime(start, '%Y-%m-%d')
        world = pytz.timezone('Europe/Minsk')
        s = timezone.make_aware(time_start, world)
        finish = request.POST.get('finish')
        time_finish = datetime.strptime(finish, '%Y-%m-%d')
        worlds = pytz.timezone('Europe/Minsk')
        fi = timezone.make_aware(time_finish, worlds)
        try:
            model = models.Projects_men(us_manager=request.user, name=name, men_email=email, photo=image, pay=number, date_start=s, date_finish=fi, social_category=type_social, pay_category=type_pay, stat=status)
            model.save()
            return redirect('projects_m')
        except:
            error = 'Ошибка отправки'
            return render(request, 'project_m.html',{'error':error})

    try:
        dan = models.Projects_men.objects.all()
    except:
        error = 'Ошибка'
        return render(request, 'project_m.html', {'error': error})
    return render(request, 'project_m.html', {'dan':dan})





