# Generated by Django 3.2.9 on 2021-11-15 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profileapp', '0001_initial'),
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='profileapp.student'),
        ),
    ]
