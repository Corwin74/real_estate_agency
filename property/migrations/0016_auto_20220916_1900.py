# Generated by Django 2.2.28 on 2022-09-16 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220916_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'Жалоба', 'verbose_name_plural': 'Жалобы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Владелец', 'verbose_name_plural': 'Владельцы'},
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL),
        ),
    ]