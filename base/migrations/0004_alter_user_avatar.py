# Generated by Django 4.1 on 2022-09-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/avatar.svg', null=True, upload_to=''),
        ),
    ]
