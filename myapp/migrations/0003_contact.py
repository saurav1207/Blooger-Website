# Generated by Django 3.2.10 on 2022-03-31 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_blog_short_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
