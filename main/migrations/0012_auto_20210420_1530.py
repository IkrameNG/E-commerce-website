# Generated by Django 3.1.8 on 2021-04-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210420_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Vetement', 'Vetement')], max_length=200, null=True),
        ),
    ]