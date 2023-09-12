# Generated by Django 4.2.4 on 2023-08-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volunteer", "0004_alter_volun_region_alter_volun_writer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="volun",
            name="region",
            field=models.CharField(
                choices=[
                    ("gangwon", "강원도"),
                    ("chungcheong", "충청도"),
                    ("metropolitan", "광역시"),
                    ("jeolla", "전라도"),
                    ("jeju", "제주도"),
                    ("gyeonggi", "경기도"),
                    ("gyeongsong", "경상도"),
                    ("seoul", "서울"),
                ],
                max_length=400,
                null=True,
            ),
        ),
    ]