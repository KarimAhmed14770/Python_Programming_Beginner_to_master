#match case is similar to switch statement in c or c++
day_no=int(input('enter day number: '))
match day_no:
    case 1:
        print('Saturday')
    case 2:
        print('Sunday')
    case 3:
        print('Monday')
    case 4:
        print('Tuesday')
    case 5:
        print('Wednesday')
    case 6:
        print('Thursday')
    case 7:
        print('Friday')
    case _:
        print('invalid number')