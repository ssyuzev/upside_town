# Generated by Django 3.2.4 on 2021-06-11 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_like'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('from_person', 'to_person')},
        ),
    ]