from random import Random
from django.core.mail import send_mail
from Shopping.models import EmailVerfiRecord
from ONline.settings import  EMAIL_FORM


def random_str(randomlegth=8):
    string = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlegth):
        string += chars[random.randint(0, length)]
    return string

def send_register_email(email, send_type="register"):
    email_record = EmailVerfiRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_title = "在线商城注册激活链接"
        email_body = "请点击下面的链接激活你的账户：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FORM, [email])
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "在线商城重置密码连接"
        email_body = "请点击下面的链接重置你的密码：htpp://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FORM, [email])
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "在线商城邮箱修改验证码"
        email_body = "你的邮箱验证码为：{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FORM, [email])
        if send_status:
            pass

