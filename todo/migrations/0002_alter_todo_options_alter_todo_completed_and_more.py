# Generated by Django 5.1.4 on 2025-06-21 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created_at'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False, help_text='Mark if the task is completed'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, help_text='Add any additional details about the task'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(help_text='Enter a clear and concise task title', max_length=200, validators=[django.core.validators.MinLengthValidator(3, 'Title must be at least 3 characters long')]),
        ),
    ]
