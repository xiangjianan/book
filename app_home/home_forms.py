from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from app_home.models import Book


# add作者
class AddFormAuth(forms.Form):
    auth_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '作者名字'}))


# add出版社
class AddFormPub(forms.Form):
    pub_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '出版社名字'}))


# add书
class AddFormBook(forms.Form):
    book_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '书名'}))

    def clean_book_name(self):
        val = self.cleaned_data.get('book_name')
        ret = Book.objects.filter(book_name=val)
        if not ret:
            return val
        else:
            raise ValidationError('图书已存在')
