# Generated by Django 3.0.3 on 2020-02-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='label',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]