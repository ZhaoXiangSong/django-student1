import hashlib
from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
# Create your views here.
def index(request):
    # 假设 服务端判断 requset.cookie['session_id'],没有session_id没有或不正确则禁止登录，重定向到登录
    # print(request.session['is_login'])
    return render(request, 'login/index.html', context={})  # 成功返回首页

def register(request):
    """GET 返回注册表单"""
    if request.method == 'GET':
        return render(request,'login/register_ajax_raw.html',context={})
    elif request.method == 'POST':
        context = {}
        name = request.POST['name']
        password = request.POST['password']
        # 密码加密
        md5 = hashlib.md5()
        md5.update(password.encode())
        hash_password = md5.hexdigest()
        # 验证 用户名、密码是否在长度范围内 len()  # 判断字符串纯中文
        # if len(name) <= 1:
        #     context['error_message'] = '用户名太短'
        #     return render(request,'login/register.html',context)
        # return render(request,'login/register.html',context)  # 失败

        user = User(name=name,password=password,hash_password=hash_password)
        user.save()
        return redirect(to='/login/index/')  # 成功返回首页

def register_check(request):
    """检查注册参数，返回json结果
    :param  客户端的表单请求
    :method 请求方式 POST
    :return json格式的字符串
    ,
    {
        "code":100,          # 200成功
        "status":"faild",    # ok成功
        "error_message":"",     # 用户名太短  等...
    }
    """
    import json
    resp_obj = {}
    name = request.POST['name']
    # if len(name) < 8 :
    if len(name) <= 1:
        # error_message = '用户名太短'
        resp_obj = {
            'code' : 100,
            'status':'验证失败',
            'error_message':'用户名太短',
        }
        resp_json = json.dumps(resp_obj)
        print(type(resp_obj))
        print(type(resp_json))
        return HttpResponse(resp_json)
def do_register(request):
    pass
def verify(request):
    # 较深颜色
    color = (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))
    # 较浅颜色
    color2 = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
    # 白色画布
    image = Image.new('RGB', size=(240, 60), color=(255, 255, 255))
    font = ImageFont.truetype('arial.ttf', 36)
    # 生成绘制的对象
    draw = ImageDraw.Draw(image)
    for x in range(2, 241):
        for y in range(0, 60):
            draw.point(xy=(x, y), fill=(color2))
    letter1 = []
    for t in range(0, 4):
        letter = chr(random.randint(65, 90))
        letter1.append(letter)
        draw.text((60 * t + 20, 10), letter, font=font, fill=color)
    print(letter1)
    image = image.filter(ImageFilter.BLUR)
    image.save('media/photo.jpg', 'jpeg')
    # img = 'photo.jpg'

def login(request):
    if request.method == 'GET':
        # 较深颜色
        color = (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))
        # 较浅颜色
        color2 = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
        # 白色画布
        image = Image.new('RGB', size=(240, 60), color=(255, 255, 255))
        font = ImageFont.truetype('arial.ttf', 36)
        # 生成绘制的对象
        draw = ImageDraw.Draw(image)
        for x in range(2, 241):
            for y in range(0, 60):
                draw.point(xy=(x, y), fill=(color2))
        letter1 = []
        for t in range(0, 4):
            letter = chr(random.randint(65, 90))
            letter1.append(letter)
            draw.text((60 * t + 20, 10), letter, font=font, fill=color)
        print(letter1)
        # for i in letter1:
        #     let = i
        letter10 = letter1[0]
        letter11 = letter1[1]
        letter12 = letter1[2]
        letter13 = letter1[3]
        letter1 = letter10 + letter11 + letter12 + letter13
        print(letter1)
        image = image.filter(ImageFilter.BLUR)
        image.save('media/photo.jpg', 'jpeg')
        # img = 'photo.jpg'
        return render(request,'login/login.html',context={'letter':letter1})
    elif request.method == 'POST':
        context = {}
        name = request.POST['name']
        password = request.POST['password']
        verify = request.POST['verify']
        letter = request.POST['letter']
        if verify == letter:
            # 密码加密  # 也可以 from django.contrib.auth.hashers import make_password,check_password
            user_list = User.objects.filter(name=name,password=password)    # 多个where条件可以逗号分隔，代表and 连接条件。
            # 多条件可以用Q对象 from django.db.models import Q
            # User.objects.filter(Q(nme=1111)&Q(password=1111))   &表示为and，并且的意思
            if user_list:
                # 登录成功

                #
                # user_list[0].name + time.now()   通过hash生成session_id
                # return HTTOResponse set_cookie {'session_id':'slaisdj12;l@;l'}
                # 客户端接收到响应 根据set_cookie响应头把数据存到自己的cookie中
                # 之后客户端每一次请求，都会带上cookie，服务端就会比对是否存在，存在即用户已登录
                # django已经封装了方法，我们可以简单在响应头里设置cookie,下一个请求的视图函数就可以取到值
                request.session['is_login'] = True
                request.session['username'] = user_list[0].name
                request.COOKIES['is_login'] = True
                request.COOKIES['username'] = user_list[0].name
                return redirect(to='/login/User1/')
            else:
                # 登录失败
                if User.objects.filter(name=name).exists():
                    context['message'] = '老铁，密码错了'
                    return render(request,'login/login.html',context)

                else:
                    context['message'] = '老铁你用户名都不存在呀，先注册吧'
                    return render(request,'login/login.html',context)
                    # return redirect(to='/login/register/')
        else:
            message1 = '验证码错误'
            context = {
                'message1':message1
            }
            return render(request,'login/login.html',context)

def do_login(request):
    pass
def User1(request):
    return render(request,'login/User1.html',context={})
def logout(request):
    request.session.flush()   # 清楚session
    # 统计在线人数，读django——session表行数。自己测试主要用不用的浏览器使用
    pass
def do_lggout(request):
    pass

