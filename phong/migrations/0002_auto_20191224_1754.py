# Generated by Django 2.2.6 on 2019-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phong', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phong',
            name='loaiphong',
            field=models.IntegerField(choices=[(3, 'Phòng trẻ em'), (1, 'Phòng đơn'), (0, 'Phòng cao cấp Loại 1'), (2, 'Phòng đôi')], default=0),
        ),
    ]