# Generated by Django 4.2.7 on 2023-11-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_text_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]