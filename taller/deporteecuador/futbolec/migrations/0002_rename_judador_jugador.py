# Generated by Django 4.2.2 on 2023-06-17 22:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("futbolec", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Judador",
            new_name="Jugador",
        ),
    ]