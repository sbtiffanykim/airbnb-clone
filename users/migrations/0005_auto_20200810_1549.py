# Generated by Django 2.2.5 on 2020-08-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200810_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('other', 'Other'), ('female', 'Female'), ('male', 'Male')], max_length=10),
        ),
    ]
