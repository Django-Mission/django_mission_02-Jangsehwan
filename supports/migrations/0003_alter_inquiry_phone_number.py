# Generated by Django 4.0.3 on 2022-04-19 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supports', '0002_alter_faq_last_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='답변수신 폰번호'),
        ),
    ]