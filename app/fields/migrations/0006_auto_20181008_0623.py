# Generated by Django 2.1.2 on 2018-10-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0005_auto_20181008_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='name',
            field=models.CharField(max_length=60, verbose_name='이름'),
        ),
    ]