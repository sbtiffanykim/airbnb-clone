# Generated by Django 2.2.5 on 2020-08-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('other', 'Other'), ('female', 'Female'), ('male', 'Male')], max_length=10),
        ),
    ]
