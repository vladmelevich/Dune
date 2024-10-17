from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Projects_men(models.Model):
    us_manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user')
    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='imag/')
    pay = models.IntegerField()
    men_email = models.EmailField(null=True, blank=True)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    social_category = models.CharField(max_length=45)
    pay_category = models.CharField(max_length=10)
    stat = models.CharField(max_length=15)

class Bloger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='imag/')
    name_first = models.CharField(max_length=255)
    tel_num = models.IntegerField()
    us_email = models.EmailField()
    social_net = models.CharField(max_length=45)
    subs = models.CharField(max_length=45)
    num = models.IntegerField()
    tem = models.CharField(max_length=45)

class Applications(models.Model):
    pr = models.ForeignKey(Projects_men, on_delete=models.CASCADE, related_name='pr')
    blog = models.ManyToManyField(Bloger,related_name='blog')
    applicat = models.CharField(max_length=45, default='Отправлено')
    kol = models.IntegerField(default=0)

#class price(models.Model):
    #zarabot = models.IntegerField(default=0)

class Posts(models.Model):
    projects_post = models.OneToOneField(Applications, on_delete=models.CASCADE,related_name='apl_blog_us')
    date_nach = models.DateTimeField(default=timezone.now)
    data_konec = models.DateTimeField(default=timezone.now)
    format = models.CharField(max_length=500, default='Н/Д')
    work_url = models.URLField()
    kol_p = models.IntegerField(default=0)
