'''
Included in standard lib but needs to be imported
'''
import itertools as it
import operator

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)
'''
itertools.accumulate(iterable[, func, *, initial=None])
Default behavior is that it applies operator.add func on 2 elements. Any func of 2 arguments can be applied.
'''
accumulate_data = [2,3,4,23,55,77,22]
print ("Default behavior of add 2 elements of ", accumulate_data)
print (list(it.accumulate(accumulate_data)))
print ("Changing Default behavior of add to multiply for", accumulate_data)
print (list(it.accumulate(accumulate_data, operator.mul)))
print ("Finding the larger of 2 elements for ", accumulate_data)
print (list(it.accumulate(accumulate_data, max)))
print ("=" * 50)
print ("*" * 50)
print ("=" * 50)
'''
itertools.combinations(iterable, r)
Takes an iterable and a integer. This will create all the unique combination that have r members.
Combination tuples are emitted in lexicographic ordering according to the order of the input iterable. So, if the input iterable is sorted, the output tuples will be produced in sorted order.
combinations('ABCD', 2) --> AB AC AD BC BD CD
combinations(range(4), 3) --> 012 013 023 123
'''
mystr_combinations = "MYSTUFF"
print ("Combination for string in 3 char each", mystr_combinations)
results_combinations = it.combinations(mystr_combinations,3)
for i in results_combinations:
    print (i)
mylst_combinations = ["apple", "orange", "cinnamon", "nutmeg"]
print ("Example for a list in combination of 2 for",mylst_combinations)
results_lst_combinations = it.combinations(mylst_combinations,2)
for i in results_lst_combinations:
    print (i)

'''
itertools.combinations_with_replacement(iterable, r)
Same as combinations but allows individual elements to be repeated more than once in combinations.
'''
mylst_combinations = ["apple", "orange", "cinnamon", "nutmeg"]
print ("Example for a list in combination_with_replacement of 2 for",mylst_combinations)
results_lst_combinations = it.combinations_with_replacement(mylst_combinations,3)
for i in results_lst_combinations:
    print (i)

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
itertools.count(start=0, step=1)
Makes an iterator that returns evenly spaced values starting with number start.
Often used as an argument to map() to generate consecutive data points. Also, used with zip() to add sequence numbers.
'''
print ("Example 1:")
for i in it.count(1,2):
    print (i)
    if i > 20:
        break

print ("Example 2:")
mylist = ['John', 'Marie', 'Jack', 'Anna']
for i in zip(it.count(), mylist):
    print(i)

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
itertools.cycle(iterable)
# cycle('ABCD') --> A B C D A B C D A B C D ...
Repeats indefinitely unless a loop break condition is defined. 
'''
mylist = [1,2,3,4]
count = 0
for i in it.cycle(mylist):
    print(i)
    count += 1
    if count > 20:
        break

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)
'''
itertools.chain(*iterables)
# chain('ABC', 'DEF') --> A B C D E F
chain multiple iterables together, by generating an iterator that traverses them sequentially, one after the other
'''
result = it.chain([1, 2, 3], ["one", "two", "three"], "String", ("this", "is", "a", "tuple"))
        
for i in result:
    print (i)

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
itertools.compress(data, selectors)
# compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
Prints the values after ZIP of 2 list, one with data other with truthy/falsy
'''
mylist_comp = [2,4,5,6,8,10]
results_comp = it.compress(mylist_comp, map(lambda x: x % 2 == 0, mylist_comp))
print (*results_comp, end="\n")

#OR
print ("Ex 2:")
mylist_comp = [2,4,5,6,8,10]
selector = [1,1,0,1,1,1]
results_comp = it.compress(mylist_comp, selector)
print (*results_comp, end="\n")

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
dropwhile()
#dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, RETURNS EVERY ELEMENTS EVEN IF PREDICATE IS TRUE..
'''
print ("#dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1")
mylist_comp = [2,4,5,6,8,10,3]
results_comp = it.dropwhile(lambda x: x <= 6, mylist_comp)
print (*results_comp, end="\n")

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
filterfalse()
# filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
Makes an iterator that filters elements from iterable returning only those for which the predicate is False.
'''
print ("# filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8")
mylist_comp = [2,4,5,6,8,10,3]
results_comp = it.filterfalse(lambda x: x % 2, mylist_comp)
print (*results_comp, end="\n")

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
groupby()

Simply put, this function groups things together if they pass the condition and are next to each other.
'''
print ("# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D")

from itertools import groupby
mystr = "aaabbbbbbbbssssbeeeeeefffffffffggggggggg"
for k,v in groupby(mystr,lambda x: x.upper()):
    print (k, len(list(v)))

print ("Ex 2:")

humans = [
    {"name": "Jin", "origin": "CN"},
    {"name": "Yun", "origin": "KR"},
    {"name": "manish", "origin": "IN"},
    {"name": "malik", "origin": "IN"},
    {"name": "Lee", "origin": "KR"},
]
for key, group in it.groupby(humans, key=lambda x: x['origin']):
    print(key)
    print(list(group))

print ("=" * 50)
print ("*" * 50)
print ("=" * 50)

'''
islice()
allows you to cut out a piece of an iterable.
itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])
# islice('ABCDEFG', 2) --> A B
# islice('ABCDEFG', 2, 4) --> C D
# islice('ABCDEFG', 2, None) --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G
'''

print ("islice('ABCDEFG', 2, None) --> C D E F G")

mystr = "AAABBBCCCDDDEEEFFF"
print (*list(it.islice(mystr,0,None,3)))

https://www.pythoncheatsheet.org/modules/itertools-module permutations
