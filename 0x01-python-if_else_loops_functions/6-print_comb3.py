#!/usr/bin/python3
print(*['{:02d}'.format(i) for i in range(10)
        for j in range(i+1, 10)], sep=', ')
