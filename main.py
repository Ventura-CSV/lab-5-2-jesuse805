def getinput(n1, n2):
    print('At function start id n1', id(n1))
    print('At function start id n2', id(n2))
    n1 = input('Enter a number')
    n2 = input('Enter a number')
    print('At function end id n1', id(n1))
    print('At function end id n2', id(n2))


def main():
    a = b = 0
    print('Before call function id n1', id(a))
    print('Before call function id n2', id(b))
    getinput(a, b)
    print('After call function id n1', id(a))
    print('After call function id n2', id(b))
    print(a, b)
    return a, b


if __name__ == '__main__':
    main()
