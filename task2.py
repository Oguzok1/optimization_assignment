import math

def f(x):
    return (x - 2)**2 + 3

def golden_section_method(f, a, b, epsilon):
    gr = (math.sqrt(5) + 1) / 2  # Golden ratio

    # Initialize points
    c = b - (b - a) / gr
    d = a + (b - a) / gr

    while abs(b - a) > epsilon:
        if f(c) < f(d):
            b = d
            d = c
            c = b - (b - a) / gr
        else:
            a = c
            c = d
            d = a + (b - a) / gr

    x_min = (b + a) / 2
    return x_min, f(x_min)

# Test the program with [a, b] = [0, 5] and ε = 1e-4
a = 0
b = 5
epsilon = 1e-4

x_min, f_min = golden_section_method(f, a, b, epsilon)
print("Approximate x_min:", x_min)
print("Approximate f(x_min):", f_min)