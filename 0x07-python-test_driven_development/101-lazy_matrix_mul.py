#!/usr/bin/python3
"""
Lazy matrix multiplication
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices m_a and m_b
    Args:
        m_a: the first matrix
        m_b: the second matrix
    """
    r = np.dot(m_a, m_b)
    return(r)
