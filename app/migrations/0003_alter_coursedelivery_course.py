# Generated by Django 4.2.5 on 2023-09-22 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_coursedelivery_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedelivery',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
    ]
