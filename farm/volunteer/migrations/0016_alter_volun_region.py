# Generated by Django 4.2.4 on 2023-08-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0015_alter_volun_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volun',
            name='region',
            field=models.CharField(choices=[('gyeongsong', '경상도'), ('metropolitan', '광역시'), ('seoul', '서울'), ('chungcheong', '충청도'), ('gyeonggi', '경기도'), ('jeolla', '전라도'), ('gangwon', '강원도'), ('jeju', '제주도')], max_length=400, null=True),
        ),
    ]
