# Generated by Django 3.2.5 on 2021-08-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0004_auto_20201124_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='tuition',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]