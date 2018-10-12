"""
Create a list nested_list consisting of five empty lists
"""
nested_list = [[], [], [], [], []]

print(nested_list)

print("Nested_list of length 5 whose items are themselves lists consisting of 3 zeros")
print("===============================================================================")
n_nested_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(n_nested_list)


print("===============================================================================")
print("list comprehansion of 3 zeroes")
print("==============================")
zero_list = [0 for dummy_idx in range(3)]
l_c_nested_list = [[0 for dummy_idx1 in range(3)] for dummy_idx2 in range(5)]
print(zero_list)
print(l_c_nested_list)


print("===============================================================================")
print("Select a specific item in a nested list")
print("==========================================")
n_l_c_nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]
print(n_l_c_nested_list[2][1])


print("===============================================================================")
print("Create a list list_dicts of 5 empty dictionaries")
print("================================================")
list_dicts = [{}, {}, {}, {}, {}]
print(list_dicts)


print("===============================================================================")
print("Function that returns a list consisting of copies of my dict")
print("============================================================")
def dict_copies(my_dict, num_copies):
	answer = []
	for idx in range(num_copies):
		answer.append(dict(my_dict))
	return answer
print(dict_copies({},5))
