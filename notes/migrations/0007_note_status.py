# Generated by Django 5.1.4 on 2024-12-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_note_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.CharField(choices=[('complete', 'Complete'), ('not_complete', 'Not Complete')], default='not_complete', max_length=255),
        ),
    ]
