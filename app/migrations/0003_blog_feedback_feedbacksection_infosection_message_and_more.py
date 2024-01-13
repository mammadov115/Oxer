# Generated by Django 5.0 on 2024-01-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_about_classes_slider_alter_contact_g_map_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/%Y/%B/%d')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='feedbacks/photos/%Y/%B/%d')),
                ('name', models.CharField(max_length=250)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FeedBackSection',
            },
        ),
        migrations.CreateModel(
            name='InfoSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='info_section/%Y/%B/%d')),
                ('google_map_embed_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('fb', 'FaceBook'), ('tw', 'Twitter'), ('in', 'Linkedin'), ('ig', 'Instagram'), ('yt', 'Youtube')], max_length=250)),
                ('link', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
