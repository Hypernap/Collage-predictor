# Generated by Django 4.1.2 on 2022-11-02 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0003_collagename_about_collagename_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collagename',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='collagename',
            name='location',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('collagename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.collagename')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
