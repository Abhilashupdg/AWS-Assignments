import json
import math
 
# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibonacci Number, else false
# n(event) is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square
def lambda_handler(event, context):
 
    # An if condition to specify to not accept numbers above 300
    if event > 300:
        return 'Invalid Entry'
    else:
        return isPerfectSquare(5*event*event + 4) or isPerfectSquare(5*event*event - 4)