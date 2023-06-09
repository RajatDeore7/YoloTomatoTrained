# Generated by Django 4.0.4 on 2023-03-08 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_videofarmimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='videofarmimages',
            options={'verbose_name': 'VideoFarmImages', 'verbose_name_plural': 'VideoFarmImagess'},
        ),
        migrations.AlterField(
            model_name='videofarmimages',
            name='image',
            field=models.ImageField(upload_to='video_farm_images'),
        ),
        migrations.AlterModelTable(
            name='videofarmimages',
            table=None,
        ),
        migrations.CreateModel(
            name='DetactFarmImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('disease_detected', models.ManyToManyField(blank=True, related_name='frame_disease', to='core.disease')),
                ('farm_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detact_farm_images', to='core.videofarmimages')),
            ],
            options={
                'verbose_name': 'VideoFarmImages',
                'verbose_name_plural': 'VideoFarmImagess',
            },
        ),
    ]
