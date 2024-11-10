from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=30,widget=forms.TextInput(attrs={'class': 'input', 'placeholder': '用户名/邮箱'}))
    password = forms.CharField(label="密码",min_length=6,widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '密码'}))

    #验证表单
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError("用户名和密码不能相同!")
        return password

#定义注册表单
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="邮箱",max_length=30,widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': '用户名/邮箱'}))
    password = forms.CharField(label='密码',min_length=6,widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '密码'}))
    #再次输入密码
    password1 = forms.CharField(label='再次输入密码',min_length=6,widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '再次输入密码'}))
    class Meta:
        model = User
        #那些字段允许修改就填哪些字段
        fields = ['email','password']

    #看用户名是否在数据库中已经存在
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('用户已存在!')
        return email

    #判断两次输入的密码一不一样
    def clean_password1(self):
        """验证密码是否相等"""
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('两次密码输入不一致！')
        return self.cleaned_data['password1']
        # password = self.cleaned_data.get('password')
        # password1 = self.cleaned_data.get('password1')
        # if password != password1:
        #     raise forms.ValidationError('两次密码不一样')
        # return password
"""创建密码修改表单类"""
class ForgetPwdForm(forms.Form):
    #邮箱字段
    email = forms.EmailField(label='请输入注册邮箱地址',max_length=30,widget=forms.EmailInput(attrs={'class':'input', 'placeholder': '用户名/邮箱'}))

class ModifyPwdForm(forms.Form):
    """修改密码表单"""
    password = forms.CharField(label='请输入新密码',min_length=6,widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '请输入新密码'}))


class UserForm(forms.ModelForm):
    """user表单，只允许修改Email"""
    class Meta:
        model = User
        fields = ['email',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nike_name','desc','gexing','birthday','gender','address','image']