import sys

digit_string = sys.argv[1]

for i in range(1, int(digit_string) + 1):
    print(' ' * (int(digit_string) - i) + '#' * i)