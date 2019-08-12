django 学生管理
=======
学完官网投票教程后的实战项目。使用之前所有知识的综合。

任务：
1.创建项目
2.创建"admin","student","teacher",等app
3.student下创建表结构："student(id,no,name,age,gender,avatar,phone,class_id,teacher_id,join_time,备注)" "classes(id,no,name,grade,capacity,address)" "teacher(id,no,name,age,gender,avatar,salary,subject,address,phone)"


###### disabled可以使当前input标签失效并无法提交 
<input type="text" class="form-control" name="no"  value="{{ stu.no }}" disabled>
###### readonly可以使当前input标签设置为只读属性无法更改，提交时提交的是value里的值
<input type="text" class="form-control" name="no"  value="{{ stu.no }}" readonly>



表结构
表明 student
字段名     字段类型        注释
id          integer         表id主键
no          integer         学号          0001            (111100001111110 biginteger)    如果整数存储学号、vip会员号，考虑长度。或用字符串类型。
name        integer
age                                             （选做）约束，0-150岁
gender      integer                             small integer(0女1男)或char(4)'male' 'female'或bool（false 女 True 男） 三种设计方案均可
avatar                      头像      ''  request.POST.['file'].read() open('.jpg') write() 得到一张图表，把路径存到数据表
join_time   datetime        添加/入学时间
last_modified_time  datetime        上次修改时间
[fk]class_id        学生所在班级

class表
id
no   001
name     三年二班
grade  年级
capacity    容纳
address  xx校区xx号教学楼


teacher表
一些字段同student。可以用继承，但表较少，看表结构时还需要看两个类，这里没必要用。
salary  工资
subject     主讲科目

student-teacher   多对多
id
[fk]student_id
[fk]teacher_id
基础需求：
0.使用bootstrap成熟的web
1.放着自带的后台管理，实现学生管理（增删改查）
2.分页
追加需求：
1.excel导入导出功能
2.教师管理，班级管理
111111111111111