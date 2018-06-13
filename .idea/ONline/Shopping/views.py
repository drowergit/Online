# conding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.shortcuts import render
from django.views.generic.base import View
from Shopping.forms import LoginForm, RegisterForm, ResetPasswordForm, ModifyPwdViewForm, UserinfoForm, EmailForm, \
    SetpayForm, IdcardForm
from Shopping.models import UserProfile, EmailVerfiRecord, UserAddress
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from Shopping.utls.email_send import send_register_email
from django.core.urlresolvers import reverse

import json

# Create your views here.

# 首页
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

# 登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)                             # Form类实例化
        if login_form.is_valid():                                        # 判断是否有效
            user_name = request.POST.get('username', "")
            pass_word = request.POST.get('password', "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:                                         # 判断用户是否存在
                if user.is_active:                                       # 判断用户是否激活
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, 'login.html', {"msg": "用户未激活！"})
            else:
                return render(request, 'login.html', {"msg": "用户不存在或密码错误！"})
        else:
            return render(request, 'login.html', {"login_form": login_form})

# 注册
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():               # 判断是否正确
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):  # 判断email是否存在
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已存在"})
            pass_word = request.POST.get("password", "")
            pass_reword = request.POST.get("passwordRepeat", "")
            user_profile = UserProfile()
            user_profile.user_status = False # 默认账户没有激活
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)   # 通过django自带的make_password
            if check_password(pass_reword, user_profile.password): #通过django自带的check_password校验
                user_profile.save()
            else:
                return render(request, "register.html", {"msg": "两次输入的密码不一致"})
            # 注册成功之后发送邮件来激活
            send_register_email(user_name, "register")
            return render(request, 'login.html')

# 激活账户
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerfiRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.user_status = True
                user.save()
        else:
            return render(request, "#")
        return render(request, "login.html")

# 忘记密码
class ResetpasswordView(View):
    def get(self, request):
        return render(request, "reset_pass.html")

    def post(self, request):
        reset_form = ResetPasswordForm(request.POST)
        if reset_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "login.html")
        else:
            return render(request, "reset_pass.html", {"reset_form":reset_form})

class ResetView(View):
    def get(self, request, acitve_code):
        all_records = EmailVerfiRecord.objects.filter(code=acitve_code)
        if all_records:
            for record in all_records:
                email = record.eamil
                return render(request, "reset-password.html", {"email": email})
        else:
            return render(request, "login.html")
        return render(request, "login.html")

# 修改密码
class ModifyPwdView(View):
    def get(self,request):
        return render(request, "reset-password.html")

    def post(self, request):
        modeify_form = ModifyPwdViewForm(request.POST)
        if modeify.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return render(request, "reset-password.html", {"msg": "密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")

        email = request.POST.get("email", "")
        return render(request, "reset-password.html", {"eamil": email, "modify_form": modeify_form})

# 退出登录
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

# 个人中心
class PersonalView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, "personal.html")
        return render(request, "login.html")

# 个人信息
class UserinfoView(View):
    def get(self, request):
        return render(request, "information.html")

    def post(self, request):
        info_form = UserinfoForm(request.POST)
        if info_form.is_valid():
            nick_name = request.POST.get("nick_name", "")
            name = request.POST.get("name", "")
            gender = request.POST.get("gender", "")
            birthday = request.POST.get("birthday", "")
            mobile = request.POST.get("moblie", "")
            user_profile =UserProfile.objects.get(username=request.user.username)
            user_profile.nick_name = nick_name
            user_profile.name = name
            user_profile.gender = gender
            user_profile.birthday = birthday
            user_profile.mobile = mobile
            user_profile.save()
            return render(request, "information.html")
        return render(request, "information.html", {"msg":"输入有误"})

# 安全设置
class SafetyView(View):
    def get(self, request):
        return render(request, "safety.html")

# 修改密码
class SafetyPassview(View):
    def get(self, request):
        return render(request, 'password.html')

    def post(self, request):
        modeify_form = ModifyPwdViewForm(request.POST)
        if modeify_form.is_valid():
            pwd = request.POST.get("password", "")
            user = UserProfile.objects.get(username=request.user.username)
            if check_password(pwd, user.password):
                pwd1 = request.Post.get("password1", "")
                pwd2 = request.POST.get("password2", "")
                if pwd1 != pwd2:
                    return render(request, "password.html", {"msg":"密码不一致"})
                user = UserProfile.objects.get(username=request.user.username)
                user.password = make_password(pwd2)
                user.save()
            else:
                return render(request, "password.html", {"msg":"原密码不一致"})
        return render(request, "password.html", {"msg":"密码少于8位", "modify_form":modeify_form})

# 修改邮箱
class EmailView(View):
    def get(self, request):
        return render(request, "email.html")

    def post(self, request):
        email =  request.POST.get("email", "")
        code = request.POST.get("code", "")
        existed_records = EmailVerfiRecord.objects.filter(email=email, code=code, send_type='update_email')
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            return render(request, "step.html")
        return render(request, "email.html", {"msg":"验证码有错误"})

# 验证邮箱
class SendEmailCodeView(View):
    def get(self, request):
        email_forms = EmailForm(request.GET)
        if email_forms.is_valid():
            email = request.GET.get("email", "")
            if UserProfile.objects.filter(email=email):
                return HttpREsponse('{"status":"fail", "msg":"邮箱已存在"}', content_type="application/json")
            send_register_email(email, "update_email")
            return HttpResponse('{"status":"success"}', content_type="application/json")
        return HttpResponse('{"status":"fail", "msg":"邮箱格式不正确"}', content_type="application/json")

# 支付密码
class SetpayView(View):
    def get(self, request):
        return render(request, "setpay.html")

    def post(self, request):
        pay = SetpayForm(request.POST)
        if pay.is_valid():
            pay = request.POST.get("pay", "")
            pay1 = request.POST.get("pay1", "")
            if pay != pay1:
                return render(request, "setpay.html", {"msg":"支付密码不一致"})
            uer_pay = UserProfile.objects.get(username=request.user.username)
            user_pay.pay = make_password(pay1)
            user_pay.save()
            return render(request, "setpay.html", {"msg":"支付密码设置成功"})
        return render(request, "setpay.html", {"msg":"支付密码少于6位"})

# 实名认证
class IdcardView(View):
    def get(self, request):
        return render(request, "idcard.html")

    def post(self, request):
        card = IdcardForm(request.POST)
        if card.is_valid():
            real_name = request.POST.get("name", "")
            id = request.POST.get("id", "")
            user_real = UserProfile.objects.get(username=request.user.username)
            user_real.real_name = real_name
            user_real.name_id = id
            user_real.save()
            return render(request, "idcard.html", {"msg":"实名认证成功"})
        return render(request, "idcard.html", {"msg": "身份证大于18位或小于18位"})


# 安全问题
class QuestionView(View):
    def get(self, request):
        return render(request, "question.html")

    def post(self, request):
        pass


# 收货地址
class AddressView(View):
    def get(self, request):
        address = UserAddress.objects.filter(user=request.user)
        if address: # 此处需要判断，不然查询为空时，就会报错
            return render(request, "address.html", {"address":address})
        return render(request, "address.html")

    def post(self, request):
        add_id = request.POST.get("add_id", "")
        type = request.POST.get("type", "")
        user_add = UserAddress.objects.get(id=int(add_id))
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        district = request.POST.get("disctict", "")
        address = request.POST.get("address", "")
        if type == "delete":
            user_add = UserAddress.objects.get(id=int(add_id))
            user_add.delete()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        elif type == "default":
            # 查询当前用户的地址并全部更新为False
            UserAddress.objects.filter(user=request.user).update(default_add=False)
            user_add.default_add = True
            user_add.save()
            return HttpResponse('{"statuse":"success"}', content_type='application/json')
        elif type == "modify":
            json_data = serializers.serialize("json", UserAddress.objects.filter(id=int(add_id)), ensure_ascii=False)
            print(json_data)
            # truent JsonResponse(json_data, safe=Flse)
            return HttpResponse(json.dumps(json_data), content_type="application/json: chreset=utf-8")
        elif type == "update":
            UserAddress.objects.filter(id=int(add_id)).update(signer_name=name, signer_mobile=phone, district=district,address=address)
            return HttpResponse('{"statuse":"success"}', content_type='application/json')


class NewAddressView(View):
    def post(self, request):
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        intro = request.POST.get("intro", "")
        user_add = UserAddress()
        user_add.signer_name = name
        user_add.signer_mobile = phone
        user_add.district = address
        user_add.address = intro
        user_add.user = request.user
        user_add.save()
        return render(request, "address.html", {"msg": "收货地址添加成功"})






