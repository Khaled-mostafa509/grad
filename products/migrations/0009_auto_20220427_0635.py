# Generated by Django 3.2.5 on 2022-04-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220407_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='products',
            name='Category',
        ),
        migrations.AddField(
            model_name='products',
            name='Category',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
