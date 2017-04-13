#video_url = https://www.youtube.com/watch?v=OSGv2VnC0go
#github_url = https://gist.github.com/JeffPaine/6213790
from collections import defaultdict 
# Looping over a range of functions
for i in [0, 1, 2, 3, 4, 5]:
    print(i ** 2)
# better
for i in range(6):
    print(i ** 2)

# Looping over a collection
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(colors[i])
# better
for color in colors:
    print(color)

# Looping backwards
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])
# better
for color in reversed(colors):
    print(color)
# reversed(seq)
# Return a reverse iterator. seq must be an object which has a __reversed__()
# method or supports the sequence protocol(the __len()__() method and the 
# __getitem__() method with integer arguments starting at 0)
# Iterators are required to have an __iter__() method that returns the iterator
# object itself so every iterator is also iterable and may be used in most places
# where other iterables are accepted
# for loops accept iterables but reversed() returns a iterator. Because all iterators
# are also iterables so the better approach works

# Looping over a collection and indices
for i in range(len(colors)):
    print(i, '--->', colors[i])
# better
for i, color in enumerate(colors):
    print(i, '--->', color)

# Looping over two collections
names = ['raymond', 'rachel', 'mattew']
colors = ['red', 'green', 'blue', 'yellow']
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])
# better
for name, color in zip(names, colors):
    print(name, '--->', color)

# Looping in sorted order
# Forward sorted order
for color in sorted(colors):
    print(color)
# Backwards sorted order
for color in sorted(colors, reverse=True):
    print(color)

# Custom Sort Order
# def compare_length(c1, c2):
    # if len(c1) < len(c2): return -1
    # if len(c1) > len(c2): return 1
    # return 0
# print(sorted(colors, cmp = compare_length))
# comparison functions are no longer available in python3
# better
print(sorted(colors, key=len))

# Call a function until a sentinel value
# blocks = []
# while True:
    # block = f.read(32)
    # if block == '':
        # break
    # blocks.append(block)
# blocks = []
# for block in iter(partial(f.read, 32), ''):
    # blocks.append(block)

#  Distinguishing multiple exit points in loops
# def find(seq, target):
    # found = False
    # for i, value in enumerate(seq):
        # if value == target:
            # found = True
            # break
    # if not found:
        # return -1
    # return i
# Better
# def find(seq, target):
    # for i, value in enumerate(seq):
        # if value == target:
            # break
    # else:
        # return -1
    # return i

# Looping over dictionary keys
d = {'matthew': 'blue', 'rachel': 'green', 'raymond':'red'}
for k in d:
    print(k)
for k in list(d.keys()):
    if k.startswith('r'):
        del d[k]

# Looping over dictionary keys and values
for k in d:
    print(k, '--->', d[k])
# better
for k, v in d.items():
    print(k, '--->', v)

# Construct a dictionary from pairs
names = ['raymond', 'rachel', 'mattew']
colors = ['red', 'green', 'blue']
d = dict(zip(names, colors))
print(d)

#Counting with dictionaries
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)
# Better
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

# Grouping with dictionaries -- Part 1 and 2
names = ['raymond', 'rachel', 'mattew', 'roger',
            'betty', 'melissa', 'judith', 'charlie']
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
#  Better
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# Is a dictionary popitem() atomic?
d = {'mattew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while d:
    key, value = d.popitem()
    print(key, '--->', value)

# Linking dictionaries


