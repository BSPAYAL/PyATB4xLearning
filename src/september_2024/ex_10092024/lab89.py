#exception is a class containing other classes

#try
#   #try this code,if error
#except
#   #execute me if try has error

import math
try:
    math.exp(1000)

except Exception as e:
    print(e)
    print("enter a lower exp value")