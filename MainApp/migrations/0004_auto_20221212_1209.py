# Generated by Django 3.0.5 on 2022-12-12 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20221211_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Pizza'),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Pizza'),
        ),
    ]