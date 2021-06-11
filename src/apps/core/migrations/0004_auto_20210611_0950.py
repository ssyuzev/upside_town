# Generated by Django 3.2.4 on 2021-06-11 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_like_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='from_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_person', to='core.person'),
        ),
        migrations.AlterField(
            model_name='like',
            name='to_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_person', to='core.person'),
        ),
    ]