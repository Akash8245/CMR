# Generated by Django 5.1.6 on 2025-03-06 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_event_remove_tourstep_building_delete_building_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="branch",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        ),
    ]
