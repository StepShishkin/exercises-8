import functools

a = int(input())
b = int(input())
c = int(input())
numbers = [x for x in range(a, b+1)]

result = functools.reduce(lambda x, y: x*y, [i for i in range(a, b+1) if (i % c == 0) and (int(i**0.5)**2 == i)])

print(numbers)
print(result)
