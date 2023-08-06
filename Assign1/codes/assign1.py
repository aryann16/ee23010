import numpy as np

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])

B=np.array([-4,6])
C=np.array([-3,-5])

def dir_vec(C,B):
  return C-B

def norm_vec(C,B):
    return np.matmul(omat, dir_vec(C,B))

n=norm_vec(C,B)
pro=np.matmul(n,B)
print(n,"x=",pro)