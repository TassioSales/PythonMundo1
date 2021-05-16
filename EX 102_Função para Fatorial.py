def factorial(n , show = False):
    f = 1
    for c in range(n, 0, -1):
        print(f'{c}', end=' ')
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



print(factorial(10, show = True))