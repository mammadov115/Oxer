# Generated by Django 5.0 on 2024-01-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedbacks'},
        ),
        migrations.AlterModelOptions(
            name='infosection',
            options={'verbose_name_plural': 'Info Section'},
        ),
        migrations.AddField(
            model_name='blog',
            name='show_at_home',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='platform',
            field=models.CharField(blank=True, choices=[('fb', 'Facebook'), ('tw', 'Twitter'), ('in', 'Linkedin'), ('ig', 'Instagram'), ('yt', 'Youtube')], max_length=250, null=True, unique=True),
        ),
    ]
