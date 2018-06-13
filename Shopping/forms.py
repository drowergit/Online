from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=8, required=True)

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)

class ModifyPwdViewForm(forms.Form):
    password = forms.CharField(required=True, min_length=8)
    password1 = forms.CharField(required=True, min_length=8)
    password2 = forms.CharField(required=True, min_length=8)

class UserinfoForm(forms.Form):
    nick_name = forms.CharField(required=True, min_length=5)
    name = forms.CharField(required=True, min_length=2)
    birthday = forms.DateField(error_messages={"invalid": u"日期格式不正确"})
    mobile = forms.CharField(required=True, min_length=11)

class EmailForm(forms.Form):
    email = forms.EmailField(required=True)

class SetpayForm(forms.Form):
    pay = forms.CharField(required=True, min_length=6)
    pay1 = forms.CharField(required=True, min_length=6)

class IdcardForm(forms.Form):
    name = forms.CharField(required=True, min_length=2)
    id = forms.CharField(required=True, min_length=18, max_length=18)


