# Generated by Django 3.0.5 on 2020-10-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0004_auto_20201017_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(to='app_blog.Categorias'),
        ),
    ]
