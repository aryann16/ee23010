import numpy as np
import math
# vertices to numpy 
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
# magnitude of vector using norm command
def magnitude(vector):
    return np.linalg.norm(vector)
  #cross product
cpro=(np.cross(A-B,A-C)) 
#area
area=0.5*(magnitude(cpro))
print("the area of the triangle ABC is",area)











