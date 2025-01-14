# Generated by Django 2.2.28 on 2022-09-15 17:49

from django.db import migrations


def fill_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner, owners_phonenumber, owner_pure_phonenumber\
        in Flat.objects.values_list(
                                    'owner',
                                    'owners_phonenumber',
                                    'owner_pure_phonenumber'
                                    ).all().iterator():
        Owner.objects.get_or_create(
                                owner=owner,
                                owners_phonenumber=owners_phonenumber,
                                owner_pure_phonenumber=owner_pure_phonenumber,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220915_2047'),
    ]

    operations = [
                  migrations.RunPython(fill_owner_model)
    ]
