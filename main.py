
def get_unique_elements(input_list):
    return [element for element in input_list if input_list.count(element) <= 1]

my_list = [1, 2, 3, 1, 2, 4]
result = get_unique_elements(my_list)
print(result)