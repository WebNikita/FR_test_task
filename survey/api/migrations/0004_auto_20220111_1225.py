# Generated by Django 2.2.10 on 2022-01-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220111_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveys',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название опроса'),
        ),
    ]
