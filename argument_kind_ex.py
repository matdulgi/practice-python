def test_func(a, b):
    print(f'a : {a}, b : {b}')
    
# positional algument
test_func(1, 2)


# keyword argument
test_func(b=3, a=5)



def positional_only_arg(a, /):
    # since 3.8
    # positional and required
    print(f'{a} : a')

positional_only_arg(3)
# positional_only_arg(a=3) # can not pass keyword argument


    


    