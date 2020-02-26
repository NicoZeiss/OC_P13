# Generated by Django 3.0.3 on 2020-02-26 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('label', models.CharField(max_length=30)),
                ('is_parent', models.BooleanField(default=False)),
                ('parentcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagier.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('picture', models.URLField(blank=True)),
                ('category', models.ManyToManyField(blank=True, related_name='item', to='imagier.Category')),
            ],
        ),
    ]
