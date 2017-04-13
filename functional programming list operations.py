def my_map(callback, iterable):
    new_list = [callback(it) for it in iterable]
    return new_list

# All required parameters must be placed before any
# default arguments in Python
def my_reduce(reducer, initial_value, iterable):
    if initial_value is None:
        acc = iterable[0]
        start = 1
    else:
        acc = initial_value
        start = 0
    for index in range(start, len(iterable)):
        acc = reducer(acc, iterable[index], index, iterable)
    return acc

# 使用reduce实现compose
def compose_by_reduce(*fns):
    def inner_compose_by_reduce(result):
        return my_reduce(lambda acc, fn, index, fns: fn(acc), result, fns)
    return inner_compose_by_reduce

# 复合函数
def compose(*fns):
    def composed(result):
        for fn in reversed(fns):
            result = fn(result)
        return result
    return composed

def filter(predicate_fn, iterable):
    return [it for it in iterable if predicate_fn(it)]

# 不完全函数
def partial(fn, *presetArgs):
    def partiallyApplied(*laterArgs):
        return fn(*presetArgs, *laterArgs)
    return partiallyApplied

# binary function
def binary(fn):
    def binary_fn(*args):
        return fn(*args[0:2])
    return binary_fn

# Unique by reduce
def unique(iterable):
    def inner_unique(acc, it, index, iterable):
        if it not in acc:
            acc.append(it)
        return acc
    return my_reduce(inner_unique, [], iterable)

# flatten by reduce
def flatten(iterable, a=[]):
    def inner_flatten(acc, it, index, iterable):
        if isinstance(it, list):
            flatten(it, acc)
        else:
            acc.append(it)
        return acc
    return my_reduce(inner_flatten, a, iterable)

flat_list = flatten([1, 2, [3, 4, [5, 6, [7, 8], [[[[9, 10], [11, 12, [13, 14, [15]]]]]]]]])
print('flatten implementation using reduce', flat_list)

unique_list = unique([1, 2, 3, 4, 4, 3, 4, 2, 7, 8, 7, 8, 6])
print('unique implementation using reduce', unique_list)

binary_compose = binary(compose)

fn1 = lambda x: x * 1
fn2 = lambda x: x * 2
fn3 = lambda x: x * 3
fn4 = lambda x: x * 4
composed = binary_compose(fn1, fn2, fn3, fn4)
print('binary function ', composed(3))

composed_by_reduce = compose_by_reduce(fn4, fn3, fn2, fn1)
print('compose implementation using reduce ', composed_by_reduce(5))


my_list = my_map(lambda x: x ** 2, range(11))
print(my_list)

one = lambda : 1
two = lambda : 2
three = lambda : 3
my_list = [one, two, three]
values = my_map(lambda fn: fn(), my_list)
print(values)

my_list = filter(lambda x: x % 2 == 0, range(21))
print(my_list)

my_list = my_reduce(lambda acc, it, index, iterable: acc + it, 10, [1, 3, 5, 7, 9])
print(my_list)
