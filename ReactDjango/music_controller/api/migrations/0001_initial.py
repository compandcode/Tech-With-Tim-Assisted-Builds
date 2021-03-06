# Generated by Django 3.0.3 on 2020-12-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=0, max_length=8, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('guestCanPause', models.BooleanField(default=False)),
                ('votesToSkip', models.IntegerField(default=1)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
