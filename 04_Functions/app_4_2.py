import datetime
import random


def check_id(id):
    id = str(id)

    if len(id) != 11:
        return False

    if not id.isdigit():
        return False

    birth_year = int(id[1:3])
    birth_month = int(id[3:5])
    birth_day = int(id[5:7])

    current_date = datetime.date.today()

    if id[0] == '1' or id[0] == '2':
        birth_year += 1800
    elif id[0] == '3' or id[0] == '4':
        birth_year += 1900
    elif id[0] == '5' or id[0] == '6':
        birth_year += 2000
    else:
        return False

    try:
        birth_date = datetime.date(birth_year, birth_month, birth_day)
    except ValueError:
        return False

    if birth_date >= current_date:
        return False

    coeff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    check = sum(int(id[i]) * coeff[i] for i in range(10)) % 11

    return check == 10 or check == int(id[10])


id_number = '32608079361'  # <-- Generated from runa.lt source page.
valid = check_id(id_number)
print(f"The ID number {id_number} is {'valid' if valid else 'invalid'}.")


def generate_id():
    current_year = datetime.date.today().year
    birth_year = random.randint(current_year - 100, current_year - 18)
    birth_date = datetime.date(birth_year, random.randint(1, 12), random.randint(1, 28))

    century = ''
    gender = random.choice(['male', 'female'])
    if birth_year >= 1800 and birth_year <= 1899:
        century = '1' if gender == 'male' else '2'
    elif birth_year >= 1900 and birth_year <= 1999:
        century = '3' if gender == 'male' else '4'
    elif birth_year >= 2000 and birth_year <= 2099:
        century = '5' if gender == 'male' else '6'

    birth_date_str = birth_date.strftime('%y%m%d')

    sequence = ''.join(str(random.randint(0, 9)) for _ in range(3))

    coeff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    partial_id = century + birth_date_str + sequence
    check = sum(int(partial_id[i]) * coeff[i] for i in range(10)) % 11

    id = partial_id + str(check)

    return id


# Example usage
generated_id_number = generate_id()
print(f"Generated ID number: {generated_id_number}")
