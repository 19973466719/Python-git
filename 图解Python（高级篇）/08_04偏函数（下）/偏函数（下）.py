
def f1(a, b = 5, *args, **kwargs):
    print('a =', a, 'b =', b, 'args =', args, 'kwargs =', kwargs)

f1_new = partial(f1, 1, 3, 6, m = 8)
f1_new(2, 4, n = 9)     


def f2(a, b = 5, *, c, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'kwargs =', kwargs)

f2_new = partial(f2, 1, m = 8)
f2_new(3, c = 9)    
