
def get_keys_with_value_true(dict):
    return [key for key, value in dict.items() if value is True]

my_dict = {'a': True, 'b': False, 'c': True}
result = get_keys_with_value_true(my_dict)
print(result)