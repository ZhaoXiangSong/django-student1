# Generated by Django 2.2.3 on 2019-07-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(unique=True, verbose_name='班级号')),
                ('name', models.CharField(max_length=20, verbose_name='班级名')),
                ('grade', models.SmallIntegerField(choices=[(1, '小学一年级'), (2, '小学二年级'), (3, '小学三年级'), (7, '初中一年级')], verbose_name='年级')),
                ('capacity', models.IntegerField(verbose_name='容纳人数')),
                ('address', models.CharField(max_length=100, verbose_name='班级位置')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(unique=True, verbose_name='学号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.PositiveSmallIntegerField(verbose_name='年龄')),
                ('gender', models.SmallIntegerField(choices=[(0, '未选择'), (1, '男'), (2, '女'), (3, '保密')], default=0)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='电话号码')),
                ('avatar', models.ImageField(upload_to='image/avatar', verbose_name='头像')),
                ('join_time', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='上次修改时间')),
                ('classes', models.ManyToManyField(to='student.Class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='student.Student'),
        ),
    ]