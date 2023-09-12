# Generated by Django 4.2.4 on 2023-08-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tran", "0019_alter_cart_user_alter_tran_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tran",
            name="type",
            field=models.CharField(
                choices=[
                    ("herbs", "나물"),
                    ("grain", "곡물"),
                    ("mushroom", "버섯"),
                    ("non-specified", "기타 작물"),
                    ("vegetable", "채소"),
                    ("nuts", "견과류"),
                    ("fruits", "과일"),
                    ("root", "뿌리"),
                ],
                max_length=400,
                null=True,
            ),
        ),
    ]