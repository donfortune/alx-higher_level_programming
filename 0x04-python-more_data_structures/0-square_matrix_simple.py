#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    own_matrix = matrix.copy()

    for i in range(len(matrix)):
        own_matrix[i] = list(map(lambda x: x**2, matrix[i]))

        return (own_matrix)
