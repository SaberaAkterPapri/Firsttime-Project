# Generated by Django 3.1.2 on 2020-11-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20201108_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_create',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]