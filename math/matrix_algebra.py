# Matrix Algebra

def linear_algebra():

    import numpy as np

    A = np.array([[1.0,2.0,3.0], [2.0,7.0,4.0]])
    B = np.array([[1.0,-1.0], [0,1.0]])
    C = np.array([[5.0,-1.0], [9.0,1.0], [6.0,0]])
    D = np.array([[3.0,-2.0, -1.0], [1.0,2.0, 3.0]])
    u = np.array([[6.0, 2.0, -3.0, 5.0]])
    v = np.array([[3.0, 5.0, -1.0, 4.0]])
    w = np.array([[1.0], [8.0], [0.0], [5.0]])

    print matrix_dim("A", A)
    print matrix_dim("B", B)
    print matrix_dim("C", C)
    print matrix_dim("D", D)
    print matrix_dim("u", u)
    print matrix_dim("w", w)
    print vector_add("u", "v", u, v)
    print vector_sub("u", "v", u, v)
    print vector_scale("u",u)
    print dot_product("u","v",u, v)
    print norm("u",u)
    print add_matrix("A", "C", A, C)
    print sub_matrix("A", "C", A, C)
    print add_matrix2("C", "D", C, D)
    print matrix_mult("B", "A", B, A)
    print matrix_mult2("B", "A", B, A)
    print matrix_mult3("B", "C", B, C)
    print matrix_mult4("C", "B", C, B)
    print matrix_power("B", "4", B, 4)
    print matrix_mult5("A", "A", A, A)
    print matrix_mult6("D", "D", D, D)

def matrix_dim(s,x):

    Dim = x.shape
    Dim = "x".join(map(str, Dim))
    return str(s)+ " Dimensions: %s" %Dim

def vector_add(t,z,x,y):
    import numpy as np

    v_add = np.add(x,y)
    v_add = "".join(map(str, v_add))
    return "The addition of "+str(t)+" and "+str(z)+" is: %s" % v_add

def vector_sub(t,z,x,y):
    import numpy as np

    v_sub = np.subtract(x, y)
    v_sub = "".join(map(str, v_sub))
    return "The subtraction of " + str(t) + " and " + str(z) + " is: %s" % v_sub

def vector_scale(z, t):
    import numpy as np
    alpha = 6

    v_scale = alpha*t
    v_scale = "".join(map(str, v_scale))
    return "The scaling of " + str(z) + " by alpha is: %s" % v_scale

def dot_product(t,z,x,y):
    import numpy as np

    v_dot_product = np.vdot(x, y)
    v_dot_product = str(v_dot_product)
    return "The dot product of " + str(t) + " and " + str(z) + " is: %s" % v_dot_product

def norm(z,t):
    import numpy as np

    v_norm = np.linalg.norm(t)
    v_norm = str(v_norm)
    return "The norm(length) of " + str(z) + " is: %s" % v_norm

def add_matrix(t,z,x,y):
    import numpy as np
    try:
        result = x + y
        result = str(result)
        return "The addition of " + str(t) + " and " + str(z) + " is: %s" % result

    except ValueError:
        return "The addition of " + str(t) + " and " + str(z) + " is: not defined"

def add_matrix(t,z,x,y):
    import numpy as np
    try:
        result = x + y
        result = str(result)
        return "The addition of " + str(t) + " and " + str(z) + " is: %s" % result

    except ValueError:
        return "The addition of " + str(t) + " and " + str(z) + " is: not defined"

def sub_matrix(t,z,x,y):
    import numpy as np
    try:
        result = x - np.matrix.transpose(y)
        result = str(result)
        return "The subtraction of " + str(t) + " and " + str(z) + " transpose is: %s" %result

    except ValueError:
        return "The subtraction of " + str(t) + " and " + str(z) + " transpose is: not defined"

def add_matrix2(t,z,x,y):
    import numpy as np
    try:
        result = np.matrix.transpose(x) + (3*y)
        result = str(result)
        return "The addition of " + str(t) + " transpose and " + str(z) + " scaled by 3 " + " is: %s" %result

    except ValueError:
        return "The addition of " + str(t) + " transpose and " + str(z) + " scaled by 3 " + " is: not defined"

def matrix_mult(t,z,x,y):
    import numpy as np
    try:
        result = np.dot(x,y)
        result = str(result)
        return "The product of " + str(t) + " and " + str(z) + " is: %s" %result

    except ValueError:
        return "The product of " + str(t) + " and " + str(z) + " is: not defined"

def matrix_mult2(t,z,x,y):
    import numpy as np
    try:
        result = np.dot(x,np.matrix.transpose(y))
        result = str(result)
        return "The product of " + str(t) + " and " + str(z) + " transpose is: %s" %result

    except ValueError:
        return "The product of " + str(t) + " and " + str(z) + " transpose is: not defined"

def matrix_mult3(t,z,x,y):
    import numpy as np
    try:
        result = np.dot(x,y)
        result = str(result)
        return "The product of " + str(t) + " and " + str(z) + " is: %s" %result

    except ValueError:
        return "The product of " + str(t) + " and " + str(z) + " is: not defined"

def matrix_mult4(t,z,x,y):
    import numpy as np
    try:
        result = np.dot(x,y)
        result = str(result)
        return "The product of " + str(t) + " and " + str(z) + " is: %s" %result

    except ValueError:
        return "The product of " + str(t) + " and " + str(z) + " is: not defined"

def matrix_power(t,z, M,n):
    import numpy as np
    try:
        result = np.linalg.matrix_power(M,n)
        result = str(result)
        return "The result of " + str(t) + " raised to the " + str(z) + "th power is: %s" %result

    except ValueError:
        return "The result of " + str(t) + " raised to the " + str(z) + "th power is: not defined"

def matrix_mult5(t,z,x,y):
    import numpy as np
    try:
        result = np.dot(x,np.matrix.transpose(y))
        result = str(result)
        return "The product of " + str(t) + " and " + str(z) + " transpose is: %s" %result

    except ValueError:
        return "The product of " + str(t) + " and " + str(z) + " transpose is: not defined"

def matrix_mult6(t,z,x,y):
    import numpy as np
    try:
        result = np.dot(np.matrix.transpose(x),y)
        result = str(result)
        return "The product of " + str(t) + " transpose and " + str(z) + " is: %s" %result

    except ValueError:
        return "The product of " + str(t) + " transpose and " + str(z) + " is: not defined"

linear_algebra()

"""
A Dimensions: 2x3
B Dimensions: 2x2
C Dimensions: 3x2
D Dimensions: 2x3
u Dimensions: 1x4
w Dimensions: 4x1
The addition of u and v is: [ 9.  7. -4.  9.]
The subtraction of u and v is: [ 3. -3. -2.  1.]
The scaling of u by alpha is: [ 36.  12. -18.  30.]
The dot product of u and v is: 51.0
The norm(length) of u is: 8.60232526704
The addition of A and C is: not defined
The subtraction of A and C transpose is: [[-4. -7. -3.]
 [ 3.  6.  4.]]
The addition of C transpose and D scaled by 3  is: [[ 14.   3.   3.]
 [  2.   7.   9.]]
The product of B and A is: [[-1. -5. -1.]
 [ 2.  7.  4.]]
The product of B and A transpose is: not defined
The product of B and C is: not defined
The product of C and B is: [[ 5. -6.]
 [ 9. -8.]
 [ 6. -6.]]
The result of B raised to the 4th power is: [[ 1. -4.]
 [ 0.  1.]]
The product of A and A transpose is: [[ 14.  28.]
 [ 28.  69.]]
The product of D transpose and D is: [[ 10.  -4.   0.]
 [ -4.   8.   8.]
 [  0.   8.  10.]]
"""