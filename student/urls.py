from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('do_add/',views.do_add,name='do_add'),
    path('<int:stu_no>/delete/',views.delete,name='delete'),
    path('<int:stu_no>/do_delete/', views.do_delete, name='delete'),
    path('<int:stu_no>/update/',views.update,name='update'),
    path('<int:stu_no>/do_update/',views.do_update,name='update'),
    path('select/',views.select,name='select'),
    path('export_excel/',views.export_excel,name='export_excel'),
    path('fuzzy/',views.fuzzy,name='fuzzy'),
    path('api_index/',views.api_index,name='api_index'),
]

# 大多数情况两种方式可互换
# 方式一：如果参数就1 一个，且与业务关系较大，适合动态url匹配方式。   bili.com/av/588888/(path(av/av_id))    视图函数的参数获取到。
# 方式二：参数较多，适合query string url后?传参。
# bili.com/new/?page_no=2&page_size=20,path('news/'),视图函数中request.GET['page_no']