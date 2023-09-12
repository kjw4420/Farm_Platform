# Generated by Django 4.2.4 on 2023-08-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0013_alter_volun_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volun',
            name='region',
            field=models.CharField(choices=[('jeolla', '전라도'), ('metropolitan', '광역시'), ('gangwon', '강원도'), ('chungcheong', '충청도'), ('seoul', '서울'), ('gyeongsong', '경상도'), ('gyeonggi', '경기도'), ('jeju', '제주도')], max_length=400, null=True),
        ),
    ]