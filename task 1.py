def register(n):
    for m in range(len(n)):
        return n[m].isupper()

i = int(input()) - 1
j = int(input())
words = list(str(input()))
words = words[i:j]
print(len(list(filter(register, words))))