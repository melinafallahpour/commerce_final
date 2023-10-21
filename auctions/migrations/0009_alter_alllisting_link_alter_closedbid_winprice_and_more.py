# Generated by Django 4.1.4 on 2022-12-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_closedbid_winprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alllisting',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='closedbid',
            name='winprice',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
