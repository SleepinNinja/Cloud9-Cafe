# Generated by Django 3.2.6 on 2022-01-31 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(default=None, max_length=100000)),
                ('image', models.ImageField(default='menu type/dish-2.png', upload_to='menu type/')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('description', models.CharField(default=None, max_length=10000000)),
                ('image', models.ImageField(default='menu item/dish-3.png', upload_to='menu item/')),
                ('type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menutype')),
            ],
        ),
    ]
