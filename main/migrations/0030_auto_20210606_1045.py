# Generated by Django 3.1.8 on 2021-06-06 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0029_remove_checkout_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_carted', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='ProductsFeedBacks',
        ),
        migrations.AddField(
            model_name='order',
            name='OrderedCart',
            field=models.ManyToManyField(blank=True, to='main.OrderedCart'),
        ),
    ]
