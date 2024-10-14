import random

a = random.randint(0, 99)
b = random.randint(0, 99)
c = random.randint(0, 99)

print("Distributive Law")
print("A(B + C) -->", (a * (b + c)))
print("(A * B) + (A * C) -->", ((a * b) + (a * c)))
