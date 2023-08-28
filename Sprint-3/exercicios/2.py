num = 0

for num in range (3):
    x = int(input())
    if x % 2 == 0:
        print("Par: {}".format(x))
    else:
        print("Ímpar: {}".format(x))