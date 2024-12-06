def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(f, a, b, epsilon):
    c = (a + b) / 2.0
    while abs(f(c)) >= epsilon:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
    return c

# Test the program with [a, b] = [1, 2] and ε = 1e-6
root = bisection_method(f, 1, 2, 1e-6)
print("Approximate root:", root)
print("f(root) =", f(root))