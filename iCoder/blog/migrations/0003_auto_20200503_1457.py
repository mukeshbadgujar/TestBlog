# Generated by Django 3.0.5 on 2020-05-03 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200503_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slud',
            new_name='slug',
        ),
    ]