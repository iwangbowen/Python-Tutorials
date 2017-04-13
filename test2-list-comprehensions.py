# List comprehensions
my_list = [n for n in range(1, 11)]
print(my_list)

my_list = [n * n for n in range(1, 11)]
print(my_list)

def double(n):
    return n * 2
    
my_list = [double(n) for n in range(1, 11)]
print(my_list)

my_list = [n for n in range(1, 11) if n % 2 == 0]
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(1, 5)]
print(my_list)

# Dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# Set comprehensions
nums = [1, 3, 4, 3, 4, 5, 2, 7, 6, 6, 2, 1, 8, 9, 7, 9]
my_set = {n for n in nums}
print(my_set)

# Generator comprehensions
my_gen = (n*n for n in nums)
nums = [num for num in my_gen]
print(nums)

my_list = [print(i) for i in range(1, 11)]
print(my_list)