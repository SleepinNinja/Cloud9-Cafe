# Generated by Django 3.2.6 on 2022-01-31 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
        ),
    ]
