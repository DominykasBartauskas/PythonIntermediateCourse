multiple_types_sample = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

list_int = [x for x in multiple_types_sample if type(x) == int]
list_float = [x for x in multiple_types_sample if type(x) == float]
list_str = [x for x in multiple_types_sample if type(x) == str]
count_bool = sum(type(x) is bool for x in multiple_types_sample)

print(f'Total sum: {sum(list_int) + sum(list_float)}')
print(f'All words combined: {", ".join(list_str)}')
print(f'Booleans in list: {count_bool}')
