# Generated by Django 2.2.16 on 2022-06-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20220606_1039'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_following'),
        ),
    ]
