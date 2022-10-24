# Import numpy package
import numpy as np

# Print numpy version
print("\nNumPy version is " + np.__version__)


# ----------------------------------------------------------------
# ARRAY CREATION

# Create numpy array of size 10, filled with zeros
X = np.zeros(10)
print(X)

# Create numpy array with values from 10 to 15
X = np.arange(10, 16)
print(X)

# Create a numpy matrix of 2*2 integers, filled with ones
X = np.ones([2, 2], dtype=np.int8)
print(X)

# Create a numpy matrix of 3*2 float numbers, filled with ones
X = np.ones([3, 2], dtype=np.float16)
print(X)

# Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones
X = np.arange(4, dtype=np.int8)
Y = np.ones_like(X)
print(X)
print(Y)

# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros
X = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
Y = np.zeros_like(X)
print(X)
print(Y)

# Create a numpy matrix of 4*4 integers, filled with fives
Y = np.ones([4, 4], dtype=np.int8) * 5
print(Y)

# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens
X = np.array([[2, 3], [6, 2]], dtype=np.int8)
Y = np.ones_like(X) * 7
print(X)
print(Y)

# Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere
X = np.identity(3)
print(X)

# Create a numpy array, filled with 3 random integer values between 1 and 10
X = np.random.randint(10, size=3)
print(X)

# Create a 3*3*3 numpy matrix, filled with random float values
X = np.random.random((3, 3, 3))
print(X)

# Given the X python list convert it to an Y numpy array
X = [1, 2, 3]
Y = np.array(X)
print(X, type(X))
print(Y, type(Y))

# Given the X numpy array, make a copy and store it on Y
X = np.array([5, 2, 3], dtype=np.int8)
Y = np.copy(X)
print(X)
print(Y)

# Create a numpy array with the odd numbers between 1 to 10
X = np.arange(1, 10, 2)
print(X)

# Create a numpy array with numbers from 1 to 10, in descending order
X = np.arange(1, 10, 2)[::-1]
print(X)

# Create a 3*3 numpy matrix, filled with values ranging from 0 to 8
X = np.arange(9).reshape(3, 3)
print(X)

# Show the memory size of the given Z numpy matrix
Z = np.zeros((10, 10))
print("Show the memory size of the given Z numpy matrix")
print("%d bytes" % (Z.size * Z.itemsize))

# ----------------------------------------------------------------

# ----------------------------------------------------------------
# ARRAY INDEXATION

# Given the X numpy array, show it's first element
X = np.array(['A', 'B', 'C', 'D', 'E'])
print(X)
print(X[0])

# Given the X numpy array, show it's last element
print(X[-1])

# Given the X numpy array, show it's first three elements
print(X[0:3])

# Given the X numpy array, show all middle elements
print(X[1:-1])

# Given the X numpy array, show the elements in reverse position
print(X[::-1])

# Given the X numpy array, show the elements in an odd position
print(X[::2])

# Given the X numpy matrix, show the first row elements
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X)
print(X[0])

# Given the X numpy matrix, show the last row elements
print(X[-1])

# Given the X numpy matrix, show the first element on first row
print(X[0, 0])

# Given the X numpy matrix, show the last element on last row
print(X[-1, -1])

# Given the X numpy matrix, show the middle row elements
print(X[1:-1, 1:-1])

# Given the X numpy matrix, show the first two elements on the first two rows
print(X[:2, :2])

# Given the X numpy matrix, show the last two elements on the last two rows
print(X[2:, 2:])

# ----------------------------------------------------------------

# ----------------------------------------------------------------
# ARRAY MANIPULATION

# Convert the given integer numpy array to float
X = [-5, -3, 0, 10, 40]
print(X)
X = np.array(X, np.float16)
print(X)

# Reverse the given numpy array (first element becomes last)
X = X[::-1]
print(X)

# Order (sort) the given numpy array
X = np.sort(X)
print(X)

# Given the X numpy array, set the fifth element equal to 1
X = np.zeros(10)
print(X)
X[4] = 1
print(X)

# Given the X numpy matrix, change the last row with all 1
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X)
X[-1] = np.ones(4)
print(X)

# Given the X numpy matrix, change the last item on the last row with a 0
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X)
X[-1, -1] = 0
print(X)

# Given the X numpy matrix, add 5 to every element
X = X + 5
print(X)

# ----------------------------------------------------------------

# ----------------------------------------------------------------
# BOOLEAN ARRAY (also called masks)

# Given the X numpy array, make a mask showing negative elements
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
mask = X < 0
print(mask)

# Given the X numpy array, get the negative elements
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
mask = X < 0
X = X[mask]
print(X)

# Given the X numpy array, get numbers higher than 5
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
mask = X > 5
X = X[mask]
print(X)

# Given the X numpy array, get numbers higher than the elements mean
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
mask = X > X.mean()
X = X[mask]
print(X)

# Given the X numpy array, get numbers equal to 2 or 10
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
mask = (X == 2) | (X == 10)
X = X[mask]
print(X)

# ----------------------------------------------------------------

# ----------------------------------------------------------------
# LOGIC FUNCTION

# Given the X numpy array, return True if none of its elements is zero
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
print(X.all())

# Given the X numpy array, return True if any of its elements is zero
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(X)
print(X.any())

# ----------------------------------------------------------------

# ----------------------------------------------------------------
# SUMMARY STATISTIC

# Given the X numpy array, show the sum of its elements
X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
print(X)
print(X.sum())

# Given the X numpy array, show the mean of its elements
X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
print(X)
print(X.mean())

# Given the X numpy matrix, show the sum of its columns and rows
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X)

print(X.sum(axis=0))  # Column
print(X.sum(axis=1))  # Rows

# Given the X numpy matrix, show the mean of its columns and rows
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X)

print(X.mean(axis=0))  # Column
print(X.mean(axis=1))  # Rows

# Given the X numpy array, show the max value of its elements
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X)

print(X.max())
