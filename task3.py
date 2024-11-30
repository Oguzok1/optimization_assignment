def f(x):
    return -x**2 + 4*x + 1

def df(x):
    return -2*x + 4

def gradient_ascent(f, df, x0, alpha, N):
    x = x0
    for _ in range(N):
        x += alpha * df(x)
    return x, f(x)

# Test the program with x0 = 0, alpha = 0.1, and N = 100
x0 = 0
alpha = 0.1
N = 100

x_max, f_max = gradient_ascent(f, df, x0, alpha, N)
print("Approximate x_max:", x_max)
print("Approximate f(x_max):", f_max)