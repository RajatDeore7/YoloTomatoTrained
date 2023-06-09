# Generated by Django 4.0.4 on 2023-03-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_farmvideo_moisture_farm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ph_farm_less', models.PositiveBigIntegerField()),
                ('ph_farm_more', models.PositiveBigIntegerField()),
                ('moisture_farm_less', models.PositiveBigIntegerField()),
                ('moisture_farm_more', models.PositiveBigIntegerField()),
                ('total_amt_salt_farm_less', models.PositiveBigIntegerField()),
                ('total_amt_salt_farm_more', models.PositiveBigIntegerField()),
            ],
        ),
    ]
