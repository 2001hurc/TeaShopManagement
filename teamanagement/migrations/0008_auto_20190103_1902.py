# Generated by Django 2.1.4 on 2019-01-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamanagement', '0007_commodity_info_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('today', models.CharField(max_length=50)),
                ('ismember', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('discount', models.IntegerField(default=100)),
                ('original_price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tea_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tea_name', models.CharField(max_length=50)),
                ('tea_cost', models.FloatField()),
                ('tea_price', models.FloatField()),
                ('tea_composition', models.CharField(max_length=50)),
                ('tea_sugar', models.CharField(choices=[('free', 'free'), ('normal', 'normal'), ('full', 'full')], max_length=10)),
                ('tea_temperature', models.CharField(choices=[('cold', 'cold'), ('normal', 'normal'), ('hot', 'hot')], max_length=10)),
                ('tea_additional', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='commodity_info',
            name='commodity_id',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='commodity_id',
        ),
    ]
