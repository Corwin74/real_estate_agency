import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_agency.settings')
django.setup()


from property.models import Flat
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

normalized_numbers = []
for flat in Flat.objects.all().iterator():
    try:
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
    except NumberParseException:
        print('Not valid', parsed_number)
        continue
    if not phonenumbers.is_valid_number(parsed_number):
        continue
    normalized_numbers.append(phonenumbers.format_number(
                                    parsed_number,
                                    phonenumbers.PhoneNumberFormat.E164
                                                        )
                             )
with open('file.txt', 'w') as f:
    for line in normalized_numbers:
        f.write(f'{line}\n')
