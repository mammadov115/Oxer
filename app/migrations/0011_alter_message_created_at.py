# Generated by Django 5.0 on 2024-01-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_blog_options_alter_feedback_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name='Sending Date'),
        ),
    ]
