from math import ceil
from django.shortcuts import render,redirect
from .models import Student,Class       # from.models import * # from .import models
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.db.models import Q

from django.db.models import Max
# Create your views here.
def index(request):
    """获取学生列表"""
    # 计算分页索引
    page_no = int(request.GET.get('page_no',1))
    page_size = int(request.GET.get('page_size',3))
    start_index = (page_no - 1) * page_size
    end_index = page_no * page_size

    # todo  多条件过滤
    # name_like = "明"  gender="女"
    # 查询
    rows_amount = Student.objects.all().count()
    # page_amount = rows_amount//page_size + 1   #9条/ 每页3条 整除时导致总页数多算了1。解决方法1 行数-0.1再除； 方法2 ceil 返回大于等于的整数
    page_amount = ceil(rows_amount / page_size)
    page_amount_list = [i for i in range(page_amount)]
    # if page_size > page_amount or page_size < 0 :
    #     error_message = '请求页码数超过最大页码'
    # if page_no >= page_amount:
    #     page_no = page_no
    student_list = Student.objects.all().order_by('no')[start_index:end_index]
    context = {
        'student_list':student_list,
        'page_amount_list':page_amount_list,
        'page_no':page_no,
        # 'Paginator':
        'page_previous':page_no - 1 or 1,
        'page_next':page_no + 1
    }
    return render(request,'student/index.html',context)
def add(request):
    # student = Student.objects.all()
    # print(student)
    # context = {
        # 'student1':student
    # }
    # 获取生成下一个学号
    max_no = Student.objects.aggregate(Max('no'))   # {'no__max': 7}
    next_no = max_no['no__max'] + 1
    # SELECT  max(id) as max_id  from student_student;
    context = {
        'next_no': next_no,
    }
    return render(request,'student/add.html',context)
def do_add(request):
    assert request.method == 'POST','error:表单http请求方式应为post'
    a = request.POST
    file = request.FILES
    print(file)
    no = a['no']
    name = a['name']
    age = a['age']
    gender = a['gender']
    phone = a['phone']
    new_img = file['avatar']

    # new_img_name = '%s/%s'%(settings.MEDIA_ROOT,new_img.name)
    # with open(new_img_name,'wb')as f:
    #     for fimg in new_img.chunks():
    #         f.write(fimg)
    #         f.close()
    print('上传成功')

    new_stu = Student()
    new_stu.avatar =new_img
    new_stu.no = no
    new_stu.name = name
    new_stu.age = age
    new_stu.gender = gender
    new_stu.phone = phone
    new_stu.save()
    context = {}
    return render(request,'student/success.html',context)
def delete(request,stu_no):
    student = Student.objects.get(no=stu_no)
    # print(student)
    context = {
        'stu':student
    }
    return render(request,'student/delete.html',context)
def do_delete(request,stu_no):
    # a = request.POST
    # print(a)
    aa = Student.objects.get(no=stu_no).delete()
    # print(aa)
    # context = {}
    return HttpResponseRedirect('http://127.0.0.1:8000/student/index/')
def update(request,stu_no):
    student = Student.objects.get(no=stu_no)
    context = {
        'stu':student
    }
    return render(request,'student/update.html',context)
def do_update(request,stu_no):
    assert request.method == 'POST','error:表单http请求方式应为post'
    a = request.POST
    file= request.FILES
    no = a['no']
    name = a['name']
    age = a['age']
    gender = a['gender']
    phone = a['phone']
    new_img = file['avatar']
    new_student = Student.objects.get(no=stu_no)
    print(new_student)
    new_student.no = no
    new_student.name = name
    new_student.age = age
    new_student.gender = gender
    new_student.phone = phone
    new_student.avatar = new_img
    new_student.save()
    return redirect(to='/student/index/')
def select(request):
    student = Student.objects.get()
    context = {
        'student':student
    }
    return render(request,'student/select.html',context)




def export_excel(request):
    """导出所有学生信息到excel文件"""
    # 数据库查询学生数据
    # 数据拼成二维数组 （第一行为字段名，后面的为数据航飞，（选做）合并前两行、填充背景色和修改字体字号）
    # save（data，afile='media/download/student_info.xlsx'）
    # redirect(to='域名/media/download/student_info.xlsx')
    pass
def fuzzy(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['age']
        c = request.POST['gender']
        page_no = int(request.GET.get('page_no', 1))
        page_size = int(request.GET.get('page_size', 3))
        start_index = (page_no - 1) * page_size
        end_index = page_no * page_size
        # page_amount = rows_amount//page_size + 1   #9条/ 每页3条 整除时导致总页数多算了1。解决方法1 行数-0.1再除； 方法2 ceil 返回大于等于的整数
        # page_amount = ceil((rows_amount - 0.1) / page_size)
        # page_amount_list = [i for i in range(page_amount)]
        # if page_size > page_amount or page_size < 0 :
        #     error_message = '请求页码数超过最大页码'
        # if page_no >= page_amount:
        #     page_no = page_no
        # todo  多条件过滤
        # name_like = "明"  gender="女"
        # 查询
        if a=='' and b=='':
            page_no = int(request.GET.get('page_no', 1))
            page_size = int(request.GET.get('page_size', 3))
            start_index = (page_no - 1) * page_size
            end_index = page_no * page_size
            rows_amount = Student.objects.filter(gender=c).count()
            page_amount = ceil((rows_amount - 0.1) / page_size)
            page_amount_list = [i for i in range(page_amount)]
            student_list = Student.objects.filter(gender=c)[start_index:end_index]
        context = {
            'student_list': student_list,
            'page_amount_list': page_amount_list,
            'page_no': page_no,
            # 'Paginator':
            'page_previous': page_no - 1 or 1,
            'page_next': page_no + 1
        }
        return render(request, 'student/index.html', context)
    else:
        return redirect('/student/index/')

def api_index(request):
    """
    return:
    '
    {
        "code":200,
        "message":"ok",     # 没有学生数据
        "student_list":[
            ("id":1,"no":"001","name":"张三","add_time":"2019-10-9")
            ("id":1,"no":"001","name":"张三","add_time":"2019-10-9")
        ]
    }
    """





# :def cloth_sqle_line(request):
    # 后端渲染。缺点不适合做的动态图
    # 获取数据。请求其他接口读取数据库
    # 拼、要的变量
    # lengend = ;























#  分页功能原理：
# SELECT *FROM student_student LIMIT 0,3;       --学生1到3（包含3）
# SELECT * FROM student_student LIMIT 1,3;      --学生2到4
# --limit跟python中的列表切片很像但参数含义不一样。limit1,3下标（从0开始记第一行）1,3表示向后取的行数。
# SELECT  * FROM student_student LIMIT 6,3;
# SELECT  count(id) FROM student_student;   --计算总行数

# page_no 第几页  page_size 一页显示几条  page_amount 总数据个数
#           1           10
# select * from student_student limit 0,(page_size);
# 第一页 每页10条                     0   10
# 第二页                             10   10
#                                    20   10
#                               start_index = (page_no-1)*page_size
# 总页数   总行除以每页数想上取整 page_amount//page_size+1
#
# student_list = Student.objects.all().order_by('no')[1:3]
#   start_index = (page_no - 1) * page_size
#   end_index = page_no * page_size