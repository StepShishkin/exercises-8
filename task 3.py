a = int(input())
b = int(input())
c = int(input())
d = int(input())

numbers = [int(i) for i in range(a, b+1)]
print(sum(list(map(lambda x: x % c != 0 and x % 10 == d, numbers))))