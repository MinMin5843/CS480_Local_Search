import math
import random

def eggholder(x, y):
    """
    Calculates the value of the Eggholder function at a given point.
    
    Args:
        x: the x-coordinate of the input point.
        y: the y-coordinate of the input point.
    Yields:
        The value calculated at point (x,y).
    """
    term1 = -(y + 47) * math.sin(math.sqrt(abs(x/2 + (y + 47))))
    term2 = -x * math.sin(math.sqrt(abs(x - (y + 47))))
    return term1 + term2

def hill_climb_eggholder(max_no_improve=100, step_size=1.0):
    """
    Performs a desending hill-climbing search on the Eggholder function.
    
    Args:
        max_no_improve: the number of consecutive non-improving steps allowed 
                        before the algorithm terminates.
        step_size: the maximum magnitude of random perbutations applied to x and y 
                   when generating a neighboring point
    Yields:
        A tuple containing the final x- and y-coordinates reached and the minimum 
        Eggholder function value found.
    """
    # Random initial position
    x = random.uniform(-10000, 10000)
    y = random.uniform(-10000, 10000)
    best_val = eggholder(x, y)

    no_improve = 0

    while no_improve < max_no_improve:
        x_new = x + (random.random() - 0.5) * step_size
        y_new = y + (random.random() - 0.5) * step_size

        x_new = max(-10000, min(10000, x_new))
        y_new = max(-10000, min(10000, y_new))

        new_val = eggholder(x_new, y_new)

        if new_val < best_val:
            x, y = x_new, y_new
            best_val = new_val
            no_improve = 0
        else:
            no_improve += 1

    return x, y, best_val