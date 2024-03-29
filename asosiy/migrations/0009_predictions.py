# Generated by Django 4.0.5 on 2022-06-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0008_expenditure_records_income_records_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=100)),
                ('old_club', models.CharField(max_length=100)),
                ('new_club', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('value_by_tft', models.FloatField()),
                ('divergence', models.IntegerField()),
            ],
        ),
    ]
