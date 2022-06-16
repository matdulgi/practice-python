def getNumOfPeople(floor, number, mem):
    if mem[floor][number] != 0:
        return mem[floor][number]
    if floor == 0:
        return number
    if number == 2:
        return floor + 2
    if number == 1:
        return 1
        
    mem[floor][number] = getNumOfPeople(floor, number - 1, mem) + getNumOfPeople(floor - 1, number, mem)
    return mem[floor][number]


if __name__ == '__main__':
    # argument : 
    count = int(input())
    for i in range(count):
        floor = int(input())
        number = int(input())

        mem = [[0 for i in range(number + 1)] for j in range(floor + 1)]
        print(mem)
        print(getNumOfPeople(floor, number, mem))


        
        

        # if number == 1:
            # numOfPeople = 1
        # else:
            # numOfPeople = (number + )
        
        
        # 0  1  6  21 56 126
        # 0  1  5  15 35 70 126
        # 0  1  4  10 20 35 56
        # 0  1  3  6  10 15 21
        # 0  1  2  3  4  5  6

        
        
        

