# Generated by Django 4.2.7 on 2024-01-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
