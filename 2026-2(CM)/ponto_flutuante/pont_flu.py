val = int(input("Digite um valor: "))

A = 1
s = val + A

while s > val:
    A = A/2
    s = val + A

print(2*A)