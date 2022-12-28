from django.db import models

class NewsUnit(models.Model):
    GENRE_CHOICES = (
        ('更新', '更新'),
        ('活動', '活動'),
        ('其他', '其他'),
        ('公告', '公告'),
    )
    catego = models.CharField("類別", max_length=10, null=False, choices=GENRE_CHOICES)
    nickname = models.CharField("新增者", max_length=20, null=False)
    title = models.CharField("標題", max_length=50, null=False)
    message = models.TextField("訊息", null=False)
    pubtime = models.DateTimeField("公告時間", auto_now=True)
    enabled = models.BooleanField("啟用狀態", default=False)
    press = models.IntegerField("點擊次數", default=0)
    def __str__(self):
        return self.title
