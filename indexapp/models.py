import django_filters
from django.db import models
from django.utils import timezone
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
from django.conf import settings
class ProductModel(models.Model):
    GENRE_CHOICES = (
        ('最新', '最新'),
        ('精選', '精選'),
        ('普通', '普通'),
        ('其他', '其他'),
    )
    catego = models.CharField('類別', default='最新', choices=GENRE_CHOICES, max_length=5)
    pname =  models.CharField('名稱', max_length=20, null = False, blank = False)
    pauthor =  models.CharField('筆者',max_length=10, null = False, blank = False)
    add_date = models.DateTimeField('最後翻閱日期', auto_now = True)
    mod_date =  models.DateTimeField('保存日期',default = timezone.now)
    pprice = models.IntegerField('特價',blank=True, null = True,)#售價
    special_offer = models.IntegerField('原價', null = True, blank = False)#原價
    pimages = models.ImageField('圖片',upload_to='image', blank=False, null=False)
    pdescription = models.TextField('詳細介紹',max_length=600,blank=False, null = False)
    Simple_pdescription = models.TextField('簡介',max_length=150,blank=False, null = False)
    pauthor_introduce = models.TextField('筆者簡介',max_length=300,blank=True, null = True)
    pdata = models.TextField('歸類',max_length=10,blank=True, null = True)
    pcreatepeople = models.CharField('新增者',max_length=20, blank = True, null = False)
    file_title = models.CharField('檔名',blank=False, max_length = 30, null = False)
    uploadedFile = models.FileField('檔案',blank=False, upload_to = "file", null = False)
    dateTimeOfUpload = models.DateTimeField('檔案日期',auto_now = True)
    press = models.IntegerField('點擊次數',default=0)
    enabled = models.BooleanField("啟用狀態", default=True)
    pcreatepeople_email = models.CharField('新增者郵箱',blank=False, max_length = 30, null = False, default=0)

    def __str__(self):
        return self.pname

from django.db import models
from django.utils import timezone
class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)

class authorized(models.Model):
    field_mail = models.EmailField(max_length=254, null=False)
    mod_date = models.DateTimeField('保存日期',default = timezone.now)
    pprice = models.IntegerField('售價', blank=True, null=True, )  # 售價
    pname = models.CharField('名稱', max_length=20, null=False, blank=False)
    status = models.BooleanField("寄送狀態", default=False)
    pcreatepeople = models.CharField('新增者', max_length=20, blank=True, null=False)
    price_amount = models.IntegerField('收益', blank=True, null=True, )
    buyname = models.CharField('購物者', max_length=20, blank=True, null=False)
    File = models.FileField('檔案',blank=True, upload_to = "file", null = True, default = 0)