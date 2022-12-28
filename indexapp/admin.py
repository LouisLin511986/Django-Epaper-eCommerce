from django.contrib import admin
from .models import *


admin.site.site_header = '後台管理系統'  # 设置header
admin.site.site_title = '後台管理系統'  # 设置title
admin.site.index_title = '後台管理系統'


class ProductAdmin(admin.ModelAdmin):
    list_display = ("catego","pname","pauthor","add_date","mod_date","pprice","special_offer", "pcreatepeople",'enabled', "press") #,Simple_pdescripti"
    list_filter = ["catego"]
    search_fields = ("pcreatepeople","pname","pauthor",)
    ordering = ("add_date", "mod_date", "pprice", "special_offer", "press")
admin.site.register(ProductModel, ProductAdmin)

class authorizedAdmin(admin.ModelAdmin):
    list_display = ("buyname", "pname", "field_mail", "mod_date", "pprice", "price_amount", "status", "pcreatepeople")
    search_fields = ("buyname","pname","pcreatepeople",)
    ordering = ("mod_date", "pprice", "price_amount")
admin.site.register(authorized, authorizedAdmin)
