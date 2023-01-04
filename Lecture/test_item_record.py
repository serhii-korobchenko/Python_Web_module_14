
from copy import deepcopy

my_string = 'test'
second_string = 'second'
my_list =[my_string, second_string]
my_string = my_string.upper()
my_list = deepcopy(my_list)
print(my_list)