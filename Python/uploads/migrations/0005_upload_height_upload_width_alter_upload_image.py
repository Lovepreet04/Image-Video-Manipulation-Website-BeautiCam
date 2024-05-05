# Generated by Django 5.0.4 on 2024-04-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_delete_student_alter_upload_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='height',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='upload',
            name='width',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image'),
        ),
    ]
