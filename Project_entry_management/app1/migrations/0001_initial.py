# Generated by Django 2.1.7 on 2019-11-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestname', models.CharField(max_length=20)),
                ('guestemail', models.CharField(max_length=20)),
                ('guestmobileNo', models.CharField(max_length=15)),
                ('hostname', models.CharField(max_length=20)),
                ('hostemail', models.CharField(max_length=20)),
                ('hostmobileNo', models.CharField(max_length=15)),
                ('checkInTime', models.DateTimeField(auto_now_add=True)),
                ('checkOutTime', models.DateTimeField(null=True)),
                ('isCheckOut', models.BooleanField()),
            ],
        ),
    ]
