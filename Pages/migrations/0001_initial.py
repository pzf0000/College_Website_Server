# Generated by Django 2.0.2 on 2018-06-22 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ArticleManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(verbose_name='序号')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArticleManagement.Column', verbose_name='栏目')),
            ],
            options={
                'verbose_name': '页面显示栏目',
                'verbose_name_plural': '页面显示栏目',
            },
        ),
        migrations.CreateModel(
            name='DisplayImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(verbose_name='序号')),
                ('name', models.CharField(max_length=25, verbose_name='名称')),
                ('herf', models.CharField(blank=True, max_length=100, null=True, verbose_name='相对路径')),
            ],
            options={
                'verbose_name': '页面图片轮播',
                'verbose_name_plural': '页面图片轮播',
            },
        ),
        migrations.CreateModel(
            name='NavbarObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.FloatField(verbose_name='序号')),
                ('name', models.CharField(max_length=25, verbose_name='名称')),
                ('herf', models.CharField(blank=True, max_length=100, null=True, verbose_name='相对路径')),
            ],
            options={
                'verbose_name': '导航栏内容',
                'verbose_name_plural': '导航栏内容',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='页面名称')),
                ('type', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '页面显示状态',
                'verbose_name_plural': '页面显示状态',
            },
        ),
        migrations.AddField(
            model_name='navbarobject',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.Page', verbose_name='页面名称'),
        ),
        migrations.AddField(
            model_name='navbarobject',
            name='superior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pages.NavbarObject', verbose_name='上级栏目'),
        ),
        migrations.AddField(
            model_name='displayimage',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.Page', verbose_name='页面名称'),
        ),
        migrations.AddField(
            model_name='displaycolumn',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.Page', verbose_name='页面名称'),
        ),
        migrations.AlterUniqueTogether(
            name='navbarobject',
            unique_together={('page', 'serial_number')},
        ),
        migrations.AlterUniqueTogether(
            name='displayimage',
            unique_together={('page', 'serial_number')},
        ),
        migrations.AlterUniqueTogether(
            name='displaycolumn',
            unique_together={('page', 'serial_number')},
        ),
    ]
