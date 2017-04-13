def pipe(*fns):
    def piped(result):
        for fn in fns:
            result = fn(result)
        return result
    return piped

def compose(*fns):
    def composed(result):
        for fn in reversed(fns):
            result = fn(result)
        return result
    return composed

def fn1(result):
    return result + 1

def fn2(result):
    return result - 2

def fn3(result):
    return result * 3

def fn4(result):
    return result / 4

pipedfn = pipe(fn1, fn2, fn3, fn4)
composedfn = compose(fn1, fn2, fn3, fn4)
print(pipedfn(28))
print(composedfn(28))

# 不完全函数
def partial(fn, *presetArgs):
    def partiallyApplied(*laterArgs):
        return fn(*presetArgs, *laterArgs)
    return partiallyApplied

def fn5(a, b, c, d, e):
    return a * b * c * d *e

partialfn = partial(fn5, 1, 3)
print(partialfn(2, 4, 6))
            