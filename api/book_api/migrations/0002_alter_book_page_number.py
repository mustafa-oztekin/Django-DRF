# Generated by Django 4.1.3 on 2024-05-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_number',
            field=models.IntegerField(),
        ),
    ]
