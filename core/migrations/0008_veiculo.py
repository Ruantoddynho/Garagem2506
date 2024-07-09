# Generated by Django 5.0.6 on 2024-07-09 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_modelo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ano", models.IntegerField(blank=True, default=0, null=True)),
                ("preco", models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ("acessorio", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.acessorio")),
                ("cor", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.cor")),
                ("modelo", models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to="core.modelo")),
            ],
        ),
    ]