# Generated by Django 4.1.2 on 2022-10-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_collagename_cid_collagename_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collagename',
            name='about',
            field=models.TextField(default='lolo', verbose_name='nulll'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collagename',
            name='location',
            field=models.TextField(default='lolo', verbose_name='nulll'),
            preserve_default=False,
        ),
    ]
