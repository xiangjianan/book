from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from app_home.models import Book


class AddFormAuth(forms.Form):
    """ 新增作者 """
    auth_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '作者名字'}))


class AddFormPub(forms.Form):
    """ 新增出版社 """
    pub_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '出版社名字'}))


class AddFormBook(forms.Form):
    """ 新增图书 """
    book_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '书名'}))

    def clean_book_name(self):
        val = self.cleaned_data.get('book_name')
        ret = Book.objects.filter(book_name=val)
        if not ret:
            return val
        else:
            raise ValidationError('图书已存在')
