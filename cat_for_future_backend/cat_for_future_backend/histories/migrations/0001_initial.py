# Generated by Django 4.2.4 on 2023-09-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="History",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=50, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Текст історії")),
                ("date_created", models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")),
            ],
        ),
    ]
