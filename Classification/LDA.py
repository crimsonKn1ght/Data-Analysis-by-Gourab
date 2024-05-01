import numpy as np

X = np.array([
    [0.5, 3.0, 'A'],
    [1.0, 3.0, 'A'],
    [0.5, 2.5, 'A'],
    [1.0, 2.5, 'A'],
    [1.5, 2.5, 'A'],
    [4.5, 1.0, 'B'],
    [5.0, 1.0, 'B'],
    [4.5, 0.5, 'B'],
    [5.5, 0.5, 'B']
])

print(f'Table X:\n\n {X}\n')

n = X.shape[0]

# X_ = np.array([np.array(['0'] * 3)] * 10)
X_ = np.full((9, 3), 0.0)

for i in range(n):
    if X[i, 2] == 'A':
        X_[i] = np.concatenate((X[i, :2].astype(float) * -1, np.array([-1])))
    else:
        X_[i] = np.concatenate((X[i, :2].astype(float), np.array([1])))

print(f'Normalized table X:\n\n {X_}\n')

w = np.array([0.0] * 3)
f = 0               # flag will turn 1 when all we get suitable weights vector w
j = 0               # w counter

print(f'Initial w{j}: {w}\n')

while f == 0:
    for i in range(n):
        if np.dot(w, np.transpose(X_[i])) <= 0:
            w += X_[i]
            j += 1
            print(f'Fails at x{i}\nTherefore w{j} = w{j-1} + x[{i}]')
            print(f'Updated w: {w}\n')
            break
        else:
            if i == n - 1:
                f = 1
                break
            else:
                continue

print(f'Equation of the line: \n ({w[0]})x1 + ({w[1]})x2 + ({w[2]}) = 0')
