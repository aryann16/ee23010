import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])

B=np.array([-4,6])
C=np.array([-3,-5])

def dir_vec(C,B):
  return C-B

def norm_vec(C,B):
    return np.matmul(omat, dir_vec(C,B))

n=norm_vec(C,B)
pro=n@B
print(n,"x=",pro)
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
x_BC = line_gen(B,C)
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.savefig("figure")