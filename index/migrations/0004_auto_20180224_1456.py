# Generated by Django 2.0.2 on 2018-02-24 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180224_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=60),
        ),
    ]