import numpy as np
import numpy.linalg as la
import numpy.linalg.linalg as linalg
from . import show_result, print_matrix


@show_result
def exercise_2():
    A = np.matrix([[1, 2], [3, 4]])
    B = np.matrix([[-4, 3], [-2, 1]])

    print("Transposed A")
    print_matrix(A.transpose())

    print("A + B")
    print_matrix(A + B)

    print("A - B")
    print_matrix(A - B)

    print("AB")
    print_matrix(A * B)

    print("BA")
    print_matrix(B * A)


@show_result
def exercise_3():
    A = np.matrix([[1, 2], [2, 4]])
    x = np.array([[1, 2]])

    print("A•x")
    print_matrix(A * x.transpose())

    print("x^T•A")
    print_matrix(x * A)

    print("x^T•A•x")
    print_matrix(x * A * x.transpose())
