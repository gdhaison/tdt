# Generated by Django 3.0.5 on 2020-05-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200511_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]