# Generated by Django 5.0.4 on 2024-04-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('action', models.CharField(choices=[('NO_FILTER', 'nofilter'), ('COLORIZED', 'colorized')], max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
