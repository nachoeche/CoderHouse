# Generated by Django 4.2.4 on 2023-11-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(
                default=models.CharField(max_length=256), max_length=256
            ),
        ),
    ]
