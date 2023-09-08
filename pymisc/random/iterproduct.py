from itertools import product
string1 = input()
string2 = input()
list1 = list(map(int, string1.split(" ")))
list2 = list(map(int, string2.split(" ")))
prod_list = list(product(list1, list2))
print (*prod_list, end="")
