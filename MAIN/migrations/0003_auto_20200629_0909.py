# Generated by Django 3.0.7 on 2020-06-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_calon'),
    ]

    operations = [
        migrations.AddField(
            model_name='calon',
            name='suara',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='hak_pilih',
            field=models.IntegerField(default=1, editable=False),
        ),
    ]
