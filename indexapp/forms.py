from django import forms
from .models import ProductModel

class PostForm(forms.ModelForm):
    class Meta:
            model = ProductModel
            fields = '__all__'
            widgets = {
                'catego': forms.HiddenInput(),
                'pname': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '書名'}),
                'pauthor': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '筆者，限10字'}),
                'add_date': forms.HiddenInput(),
                'mod_date': forms.HiddenInput(),
                'pprice': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '售價'}),
                'special_offer': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '原價'}),
                'pimages': forms.FileInput(attrs={'class': 'form-control-file', 'style': 'width:50%;'}),
                'pdescription': forms.Textarea(attrs={'style': 'width:50%;', 'placeholder': '詳細介紹，限600字'}),
                'Simple_pdescription': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '簡單介紹，限150字'}),
                'pauthor_introduce': forms.Textarea(attrs={'style': 'width:50%;', 'placeholder': '筆者簡介，限300字'}),
                'pdata': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '書籍資訊，限10字'}),
                'pcreatepeople': forms.HiddenInput(),
                'file_title': forms.TextInput(attrs={'style': 'width:50%;', 'placeholder': '上傳檔案名稱'}),
                'uploadedFile': forms.FileInput(attrs={'class': 'form-control-file', 'style': 'width:50%;'}),
                'press': forms.HiddenInput(),
                'enabled': forms.HiddenInput(),
                'pcreatepeople_email': forms.HiddenInput(),
            }
            labels = {
                'pname': '書名',
                'pauthor': '筆者',
                'pprice': '優惠價',
                'special_offer': '原價',
                'pimages': '圖片',
                'pdescription': '詳細介紹',
                'Simple_pdescription': '簡單介紹',
                'pauthor_introduce': '筆者簡介',
                'pdata': '書籍資訊',
                'file_title': '檔案名稱',
                'uploadedFile': '檔案',
            }

from django import forms
from .models import Photo
class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }