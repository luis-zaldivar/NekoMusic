# Generated by Django 4.1.1 on 2022-11-13 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("NekoMusic", "0007_alter_playli_id_can"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playli",
            name="ID_Can",
        ),
    ]
