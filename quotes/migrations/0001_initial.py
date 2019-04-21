# Generated by Django 2.1.7 on 2019-04-04 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallons_requested', models.PositiveIntegerField()),
                ('delivery_street', models.CharField(max_length=200)),
                ('delivery_state', models.CharField(max_length=30)),
                ('delivery_zipcode', localflavor.us.models.USZipCodeField(max_length=10)),
                ('delivery_date', models.DateField()),
                ('total_amount_due', models.DecimalField(decimal_places=2, max_digits=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
