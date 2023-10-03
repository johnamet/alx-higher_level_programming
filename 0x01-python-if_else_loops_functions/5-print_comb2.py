#!/usr/bin/python3
print(''.join('0' + str(i) + ', '
              if i < 10 else str(i) + ','
              if i < 99 else str(i) + '\n'
              for i in range(0, 100)), end="")
