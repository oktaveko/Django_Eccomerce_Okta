# Generated by Django 3.2 on 2022-03-29 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220322_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
