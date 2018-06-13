from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称")
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女"), ("secrecy", u"保密")), default="male")
    pay = models.CharField(max_length=128, verbose_name=u"支付密码",default="")
    real_name = models.CharField(max_length=12, verbose_name=u"真实姓名", default="")
    name_id = models.CharField(max_length=20, verbose_name=u"身份证", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    user_status = models.BooleanField(default=True, verbose_name=u"用户状态")
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

class EmailVerfiRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"类型", choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"修改邮箱")), max_length=30)
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

class  UserAddress(models.Model):
    """用户收货地址"""
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    district = models.CharField(max_length=100, default='', verbose_name=u'区域')
    address = models.CharField(max_length=100, default='', verbose_name=u'详细地址')
    signer_name = models.CharField(max_length=100, default='', verbose_name=u'签收人')
    signer_mobile = models.CharField(max_length=11, default='', verbose_name=u'联系电话')
    default_add = models.BooleanField(default=False, verbose_name=u'默认地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"收货地址"
        verbose_name_plural = verbose_name


