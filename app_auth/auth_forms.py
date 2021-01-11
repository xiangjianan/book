from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    """
    forms组件：注册
    """
    usr = forms.CharField(min_length=2, max_length=20,
                          widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}))
    pwd = forms.CharField(min_length=3,
                          widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码（不少于3位）'}))
    r_pwd = forms.CharField(min_length=3,
                            widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '确认密码'}))

    def clean_usr(self):
        """
        检查用户名是否被注册
        :return:
        """
        val = self.cleaned_data.get('usr')
        ret = User.objects.filter(username=val)
        if not ret:
            return val
        else:
            raise ValidationError('用户已注册')

    def clean(self):
        """
        检查两次密码输入是否一致
        :return:
        """
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('密码不一致')


class UserFormLogin(forms.Form):
    """
    forms组件：登录
    """
    usr = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}))
    pwd = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))
