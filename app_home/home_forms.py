from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


# 注册
class AddFormBooks(forms.Form):
    b_id = forms.CharField(min_length=4, max_length=20,
                           widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}))
    book_name = forms.CharField(min_length=6,
                                widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))
    pub_id = forms.CharField(min_length=6,
                             widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '确认密码'}))

    def clean_usr(self):
        val = self.cleaned_data.get('usr')
        ret = User.objects.filter(username=val)
        if not ret:
            return val
        else:
            raise ValidationError('用户已注册')

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('密码不一致')


# add作者
class AddFormAuth(forms.Form):
    auth_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '作者名字'}))


# add出版社
class AddFormPub(forms.Form):
    pub_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '出版社名字'}))


# add书
class AddFormBook(forms.Form):
    book_name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '书名'}))
