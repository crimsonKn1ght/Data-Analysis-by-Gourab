# Code by Gourab Roy

import numpy as np

if __name__ == '__main__':
    X = np.array([[4.0, 11.0], [8.0, 4.0], [13.0, 5.0], [7.0, 14.0]])

    l = len(X)
    
    m = np.mean(X, axis = 0)
    X -= m

    conv_mat = np.cov(X.T)

    eigenvalues, eigenvectors = np.linalg.eig(conv_mat)

    idx = eigenvalues.argsort()[::-1]
    e1, e2 = eigenvalues[idx]
    e_vec1, e_vec2 = eigenvectors.T[idx]

    fpc = np.array([])

    for i in range(l):
        component = round(np.dot(e_vec1, X[i]), 3)
        fpc = np.append(fpc, component)
        x = str(X[i] + m)
        print(f'Component for {x:<15}: {component}')


# My first implementation of PCA (a bit longer)

# def conv(x, y, l):
#     conv_sum = 0

#     for x, y in zip(x, y):
#         conv_sum += x * y

#     conv_sum /= (l - 1)             # because we're dealing with a sample

#     return conv_sum

# if __name__ == '__main__':
#     X = np.array([[4.0, 11.0], [8.0, 4.0], [13.0, 5.0], [7.0, 14.0]])

#     l = len(X)

#     x_mean = sum(X[:, 0]) / l
#     y_mean = sum(X[:, 1]) / l
    
#     X -= (x_mean, y_mean)

#     conv_x_2 = conv(X[:, 0], X[:, 0], l)
#     conv_x_y = conv(X[:, 0], X[:, 1], l)
#     conv_y_2 = conv(X[:, 1], X[:, 1], l)

#     conv_mat = np.array([[conv_x_2, conv_x_y],
#                          [conv_x_y, conv_y_2]])
    
#     a11 = conv_mat[0, 0]
#     a12 = conv_mat[0, 1]
#     a21 = conv_mat[1, 0]
#     a22 = conv_mat[1, 1]

#     diag_sum = a11 + a22

#     det = (a11 * a22) - (a12 * a21)

#     e1, e2 = (diag_sum + np.sqrt(diag_sum**2 - 4*det)) / 2, (diag_sum - np.sqrt(diag_sum**2 - 4*det)) / 2

#     a11_e1 = a11 - e1
#     a22_e1 = a22 - e1

#     D = np.sqrt(a11_e1 ** 2 + a12 ** 2)

#     u1 = - a12 / D
#     u2 = a11_e1 / D

#     eigenvec_1 = np.array([u1, u2]).reshape((-1, 1))

#     pca_conv = []

#     for x in X:
#         pca_conv.append(np.dot(eigenvec_1.reshape((1, -1)), x.reshape((-1, 1))))


# # code by Gourab Roy
#     print("First principle Components for:" + "\n")

#     for i in range(l):
#         print(str(X[i]) + ": " + str(pca_conv[i].reshape(-1)[0]))
