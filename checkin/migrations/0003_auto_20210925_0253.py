# Generated by Django 3.2.7 on 2021-09-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0002_auto_20210924_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=256)),
                ('station_id', models.CharField(max_length=256)),
                ('action', models.CharField(max_length=64)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='station_id',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Rider',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.DeleteModel(
            name='Timesheet',
        ),
    ]
