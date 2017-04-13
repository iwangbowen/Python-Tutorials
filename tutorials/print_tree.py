import os

def print_tree(basepath, depth=-1):
    depth += 1
    for f in os.listdir(basepath):
        path = os.path.join(basepath, f)
        if os.path.isdir(path):
            print('  ' * depth + '├─{}'.format(f))
            print_tree(path, depth)
        else:
            print('  ' * depth + '└─{}'.format(os.path.basename(path)))

def skip_hidden(basepath):
    for f in os.listdir(basepath):
        if not f.startswith('.'):
            yield f

print_tree('E:')