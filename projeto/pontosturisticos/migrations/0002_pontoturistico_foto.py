# Generated by Django 3.1.6 on 2021-02-21 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontosturisticos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
