def normal_func(arg1):
    print(f'arg1 : {arg1} type: {type(arg1)} len : {len(arg1)}')
    print()

def unpack_test(*args1, **args2):
    # passed args will be unpacked
    print(f'args1 : {args1} type: {type(args1)} len : {len(args1)}')
    print(f'args2 : {args2} type: {type(args2)} len : {len(args2)}')
    print()


print(' === normal function test === ')

print(' - case : tuple')
normal_func((1,2, 3 ,4))

print(' - case : pack tuple')
try:
    normal_func(*(1,2, 3 ,4))
except TypeError as e:
    print(e)
    print()
    """ passing paking argement causes error  
    tuple passed after unpacked to 4 arguments """


print(' - case : dict')
normal_func({'a': 1, 'b': 2})

print(' - case : unpack dict')
try:
    normal_func(**{'a': 1, 'b': 2})
except TypeError as e:
    print(e)
    print()


print()
print(' === pack, unpack parameter function test === ')

print(' - case : ints')
unpack_test(1,2, 3 ,4)

print(' - case : tuple')
unpack_test((1,2, 3 ,4))

print(' - case : pack tuple')
unpack_test(*(1,2, 3 ,4))

print(' - case : dict')
unpack_test({'a': 1, 'b': 2})

print(' - case : unpack dict')
unpack_test(**{'a': 1, 'b': 2})

