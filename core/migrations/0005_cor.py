# Generated by Django 5.0.6 on 2024-06-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
    ]
