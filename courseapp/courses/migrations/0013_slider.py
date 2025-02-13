# Generated by Django 4.1.3 on 2024-05-23 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_subtitle_alter_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('isActive', models.BooleanField(default=False)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
        ),
    ]
