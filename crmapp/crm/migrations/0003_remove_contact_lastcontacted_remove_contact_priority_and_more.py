# Generated by Django 4.1.7 on 2023-02-26 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_remove_contact_age_remove_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='lastContacted',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='status',
        ),
    ]
