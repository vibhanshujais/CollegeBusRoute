# Generated by Django 5.0.7 on 2024-07-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busroutings', '0002_studentinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='busno',
            field=models.TextField(blank=True, db_column='busNo', null=True),
        ),
    ]