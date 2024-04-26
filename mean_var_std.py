'''Create a function named calculate() in mean_var_std.py that
 uses Numpy to output the mean, variance, standard deviation, 
 max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits.
 The function should convert the list into a 3 x 3 Numpy array,
   
   and then return a dictionary containing the mean, variance, standard
     deviation, max, min, and sum along both axes 
     and for the flattened matrix.'''

import numpy as np 


def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError('List must contain 9 numbers')
    matrix = np.array(numbers).reshape(3, 3)

    results = {
        'mean' : [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
        'variance' : [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
        'standard daviation' : [list(matrix.std(axis=0)), list(matrix.std(axis=0)), matrix.std()],
        'max' : [list(matrix.max(axis=0)), list(matrix.max(axis=0)), matrix.max()],
        'min' : [list(matrix.min(axis=0)), list(matrix.min(axis=0)), matrix.min()],
        'sum' : [list(matrix.sum(axis=0)), list(matrix.sum(axis=0)), matrix.sum()]
    }
    return results



numbers = list(map(int, input('Enter nine numbers seperated by a space\n').split()))
print(calculate(numbers))