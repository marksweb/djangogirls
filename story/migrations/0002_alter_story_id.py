# Generated by Django 3.2.7 on 2021-09-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("story", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
    ]
