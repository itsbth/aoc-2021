NUMBERS = [line.strip() for line in open('../input')]

current = NUMBERS
prefix = ''

while len(current) > 1:
    prefix_a = prefix + '1'
    prefix_b = prefix + '0'
    a = [num for num in current if num.startswith(prefix_a)]
    b = [num for num in current if num.startswith(prefix_b)]
    if len(a) >= len(b):
        current = a
        prefix = prefix_a
    else:
        current = b
        prefix = prefix_b

val_a = int(current[0], 2)

current = NUMBERS
prefix = ''

while len(current) > 1:
    prefix_a = prefix + '1'
    prefix_b = prefix + '0'
    a = [num for num in current if num.startswith(prefix_a)]
    b = [num for num in current if num.startswith(prefix_b)]
    if len(a) < len(b):
        current = a
        prefix = prefix_a
    else:
        current = b
        prefix = prefix_b

val_b = int(current[0], 2)

print(val_a * val_b)
