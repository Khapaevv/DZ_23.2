# Generated by Django 5.0.7 on 2024-08-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="is_publication",
            field=models.BooleanField(default=True, verbose_name="Создать?"),
        ),
    ]
