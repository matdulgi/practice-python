dict1 = dict()
dict1[0] = 0
dict1[1] = 1
dict1[2] = 2
a = 3
for i in dict1:
    print(i)
    # dict1[a] = a this code causes the RuntimeError

    
tmin=0
tmax=100
for i in range(tmin, tmax):
    print(i)
    print(tmax)
    tmax //=2



a = map(str, (1, 2, 3))
print(a)
print(list(a))

