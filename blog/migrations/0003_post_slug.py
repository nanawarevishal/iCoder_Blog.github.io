# Generated by Django 4.1 on 2022-08-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
