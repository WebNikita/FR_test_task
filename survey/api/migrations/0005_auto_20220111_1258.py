# Generated by Django 2.2.10 on 2022-01-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220111_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='survey',
        ),
        migrations.AddField(
            model_name='questions',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.Surveys', verbose_name='Опрос'),
        ),
    ]
