#!/usr/bin/python3
"""
Matrix multiplication
"""
def matrix_mul(m_a, m_b):
    """Multipling two matrix
    Args:
        m_a the first matrix and it must contain elements of int or float
        m_b the second matrix and it must contain elementsof int or float
    The column number of the first matrix must equal to the row of the second matrix.
    """
    if(type(m_a) is not list):
        raise TypeError("m_a must be a list")
    if(type(m_b) is not list):
        raise TypeError("m_b must be a list")
    if(type(m_a[0]) is not list):
        raise TypeError("m_a must be a list of lists")
    if(type(m_b[0]) is not list):
        raise TypeError("m_b must be a list of lists")
    if(m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if(m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        for m_f in range(len(m_a[0])):
            pass
    for k_f in range(len(m_b)):
        for j in range(len(m_b[0])):
            pass
    i += 1
    j += 1
    m_f += 1
    k_f += 1

    r = [[0] * j for c in range(i)]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                if (type(m_a[i][k]) is not int and m_a[i][k] is not float):
                    raise TypeError("m_a should contain only integers or floats")
                if (type(m_b[k][j]) is not int and m_b[k][j] is not float):
                    raise TypeError("m_b should contain only integers or floats")
                if (len(m_a[0]) != len(m_a[i])):
                    raise TypeError("each row of m_a must be of the same size")
                if (len(m_b[0]) != len(m_b[k])):
                    raise TypeError("each row of m_b must be of the same size")
                if (m_f is not k_f):
                    raise ValueError("m_a and m_b can't be multiplied")
                r[i][j] += m_a[i][k] * m_b[k][j] 

    return(r)
